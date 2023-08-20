from importlib import import_module
from os import listdir, system
from sys import argv
from zipfile import *

from cyaron import *
from tqdm import tqdm

if argv[0].startswith('python'):
    argv = argv[1:]

try:
    root = argv[1]
except IndexError:
    print("No Problem Id given, data generation terminated")
    exit(0)

if root.startswith('.\\') or root.startswith('./'):
    root = root[2:]

print('Problem Root:', root)
moduleRoot = root.replace('/', '.')
try:
    Config = import_module(moduleRoot + '.Config')
except Exception:
    if 'gen.py' in listdir(f'./{moduleRoot}'):
        print('Old generator found, running...')
        system(f'python3 ./{moduleRoot}/gen.py')
    else:
        print('No Config.py or gen.py found, please check the directory')
    exit(0)

print('Read Config v' + Config.version)

useConfigGen = False
try:
    useConfigGen = Config.genOut
except Exception:
    pass

validator = None
try:
    validator = Config.validator
except Exception:
    pass

compileCommand = "g++ -O3 -g -m64 -std=c++14 -Wall -o {}/std.exe {}"
try:
    compileCommand = Config.cmd
    print("Read customized compile command:", compileCommand)
except Exception:
    print("Can't read customized compile command, using default:")
    print(compileCommand)

zipName = root.split('/')[-1] + '.zip'
zipFile = ZipFile(root + '/' + zipName, 'w')


def compileCpp() -> int:
    realCpp = root + '/' + Config.std_name
    cmd = compileCommand.format(root, realCpp)
    print("Compile cmd: ", cmd)
    return system(cmd)


def main(*args, **kwargs) -> int:
    if not useConfigGen:
        retval = compileCpp()
        if retval != 0:
            print('Compile Failure')
            return 0
    if validator != None:
        # try to restructure this part if allowed
        retval = system(
            "g++ -O3 -g -m64 -std=c++14 -o {}/{} {}/{}".format(
                root, 'validator.exe', root, validator
            )
        )
        if retval != 0:
            print('Compile Failure')
            return 0
    bar = tqdm(range(1, Config.data_set + 1))
    for textGroup in bar:
        # IO Object Creation
        file = IO(
            file_prefix=root+'/',
            data_id=textGroup
        )
        # Gen Data
        if Config.version.split('.')[0] == '1':
            file.input_write(Config.generator(textGroup))
        else:
            ret = Config.Gen.generator(textGroup, file)
            if ret != None:
                file.input_write(ret)
        # Gen Output
        bar.set_description(f'Generated Input    {textGroup}')
        if not useConfigGen:
            file.output_gen(f'{root}/std.exe')
        bar.set_description(f'Generated Testcase {textGroup}')
        if validator != None:
            retval = system(
                f'./{root}/validator.exe {root}/{textGroup}.in'
            )
            if retval == 256:
                print("Data error! Please check Config.py and validator.cpp")
                return 0
            elif retval == 512:
                print("Error occurred when checking data.")
                print("Data generation terminated.")
                return 0
            else:
                bar.set_description(f'Validated Testcase {textGroup}')
        zipFile.write(
            f'{root}/{textGroup}.in', arcname=f'{textGroup}.in',
            compress_type=ZIP_DEFLATED, compresslevel=9
        )
        zipFile.write(
            f'{root}/{textGroup}.out', arcname=f'{textGroup}.out',
            compress_type=ZIP_DEFLATED, compresslevel=9
        )
    zipFile.close()
    return 0


if __name__ == '__main__':
    exit(main())
