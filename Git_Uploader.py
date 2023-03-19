try:
    from subprocess import Popen, PIPE
    from parse import compile
    from loguru import logger
    from sys import exit

except ImportError:
    from os import system
    __libs__ = [
        "subprocess",
        "loguru",
        "parse"
    ]
    for name in __libs__:
        try:
            system("pip3 install " + name)
        except Exception:
            continue

class Main:
    # 编译正则表达式
    NormalBranch  = compile("  {}\n")       # 普通的Branch样式
    CurrentBranch = compile("* {}\n")       # 标记为当前Branch的样式
    modifiedExpr  = compile("{}:   {}\n")   # git status的输出:带有文件的变化类型和名称
    def runAndGet(command:str) -> list:     # 运行指令并且获取输出
        return Popen(
            command, shell = True, stdout = PIPE
        ).stdout.readlines()

    def force_decode(route_info :str) -> str:
        # Fix: 带有中文名称的文件或者路径
        route_info = route_info.replace("\"","")    # Remove the '"'s on both sides
        retval = "."                                # 一开始为'.'
        for sec in route_info.split("/"):           # parse后, 以'/'分割路径
            sec = f"b'{sec}'"
            sec = eval(sec)                         # decode to utf-8
            retval += "/" + str(sec,encoding='utf-8')
        return retval

    def checkBranch() -> list:
        # 返回(当前branch,其他branch)
        _ret = ["",[]]
        for reads in Main.runAndGet("git branch"):
            reads = reads.decode('utf-8')
            NormalParseResult  = Main.NormalBranch.parse(reads)
            SpecialParseResult = Main.CurrentBranch.parse(reads)
            if NormalParseResult != None:           # 是一般的Branch
                _ret[1].append(NormalParseResult[0])
            else:                                   # 是当前branch
                _ret[0] = SpecialParseResult[0]
        return _ret

    def findCommits() -> list:
        _ret = []                                   # get 所有的 Commits
        commandOut = Main.runAndGet("git status")   # git status指令
        for line in commandOut:
            line = line.decode("utf-8")
            logger.info(line.replace("\n",""))      # 把最后的'\n'去掉
            __ParseResult = Main.modifiedExpr.parse(line)
            if __ParseResult != None:               # 不是特殊的行
                if not "renamed" in __ParseResult[0]:   # 不是renamed更改
                    _ret.append(__ParseResult[1])       # 获取文件名
                else:                                   # 是renamed更改
                    # 获取更改后的文件名(空格分隔后取第3个)
                    _ret.append(__ParseResult[1].split(' ')[3])
        return _ret

    def isConfirm(response: str, Default: str) -> bool:
        return response == 'Y' or response == 'y' or (response == '' and Default == 'y')

    def isDeny(response: str, Default: str) -> bool:
        return response == 'N' or response == 'n' or (response == '' and Default == 'n')

    def main(*args, **kwargs) -> None:
        logger.add("./Uploader_log/file-{time:YYYY-MM-DD}.log", retention="1 day")
        logger.info("欢迎来到Git上传工具 v2.0")
        # 首先检查当前的分支:
        CheckResult = Main.checkBranch()
        currentBranch = CheckResult[0]
        otherBranches = CheckResult[1]
        logger.info("当前分支: " + str(currentBranch))
        logger.info("其他分支: " + str(otherBranches))
        IfChange = input("是否切换到其他分支? (y/N) ")
        if Main.isConfirm(IfChange, 'n'):
            WhichToChange = input("切换到哪个分支? ")
            if WhichToChange in otherBranches:
                Main.runAndGet("git checkout " + WhichToChange)
            else:
                logger.info(f"{WhichToChange} is not in Existed Branches")
                return
        else:
            WhichToChange = currentBranch
        Main.runAndGet("git add .")
        # check which to commit
        commitResult = Main.findCommits()
        logger.info("更改过的文件: " + str(commitResult))
        for name in commitResult:
            if not name.endswith('.ttf'):
                name = name.split()[0]
            if isinstance(name, str):
                name = Main.force_decode(name)
                logger.info("Decoded: " + name)
            currentCommit = input(f"请输入对 {name} 的commit: ").replace('"','\\"')
            # 可能输入的commit中带有'"', 要在前面加 '\'
            Main.runAndGet(f'git commit "{name}" -m "{currentCommit}"')
        checkIfPush = input("是否推送到GitHub? (Y/n) ")
        if Main.isConfirm(checkIfPush, 'y'):
            Main.runAndGet("git push origin " + WhichToChange)
        if Main.isConfirm(IfChange, 'n'):
            returnToBranch = input("是否回退到原来的分支? (Y/n) ")
            if Main.isConfirm(returnToBranch, 'y'):
                Main.runAndGet("git checkout " + currentBranch)
        return

if __name__ == '__main__':
    Main.main()
    logger.info("Program exited")
    exit(0)
    