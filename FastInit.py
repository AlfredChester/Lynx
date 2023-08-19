import os
import sys


def readFile(fileName: str) -> str:
    retval = ''
    file = open(fileName, 'r', encoding='utf-8')
    for line in file.readlines():
        retval += line
    file.close()
    return retval


def writeFile(fileName: str, content: str) -> None:
    file = open(fileName, 'w', encoding='utf-8')
    file.write(content)
    file.close()


def main() -> int:
    try:
        folderName = sys.argv[1]
    except Exception:
        print("Folder name not given. Initialization terminated.")
        return 0
    os.system('mkdir ' + folderName)
    std_temp = readFile('std_template.cpp')
    spj_temp = readFile('spj_template.cpp')
    conf_temp = readFile('Config_template.py')
    val_temp = readFile('validator_template.cpp')
    writeFile(os.path.join(folderName, 'std.cpp'), std_temp)
    writeFile(os.path.join(folderName, 'Config.py'), conf_temp)
    writeFile(os.path.join(folderName, 'validator.cpp'), val_temp)
    if len(sys.argv) == 3 and sys.argv[2] == 'spj':
        writeFile(os.path.join(folderName, 'spj.cpp'), spj_temp)
    return 0


if __name__ == '__main__':
    sys.exit(main())
