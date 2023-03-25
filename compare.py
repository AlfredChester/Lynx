from importlib import import_module
from os import system

from cyaron import *

from libs.glib import args as argv

print('Usage: python compare.py {Data Generator} {program1} {program2}')
print('       {(Optional) Number of runs}')
print(f'Argv: {argv}')
try:
    root = argv[1]
except IndexError:
    print("No Problem Id given, compare terminated")
    exit(0)

if root.startswith('.\\') or root.startswith('./'):
    root = root[2:]

try:
    to_cmp = argv[2]
    std = argv[3]
    print(f"To_cmp: {to_cmp}, std: {std}")
except IndexError:
    print("To_cmp or std lost, compare terminated")
    exit(0)

try:
    number_of_runs = int(argv[4])
except IndexError:
    number_of_runs = 11 ** 4514
except:
    print("Illegal Argument(s)")
    exit(0)

print('Problem Root:', root)
moduleRoot = root.replace('/', '.')
try:
    Config = import_module(moduleRoot + '.Config')
except FileNotFoundError:
    print('No Config.py found, please check the directory')
    exit(0)

print('Read Config v' + Config.version)


def compile_source(name: str) -> int:
    cmd = f"g++ -O3 -g -m64 -std=c++14 -Wall -o {name}.exe {name}"
    print("Compile cmd: ", cmd)
    return system(cmd)


def main(*args, **kwargs) -> int:
    run_set = 1
    compile_source(to_cmp)
    compile_source(std)
    to_cmp_exe = './' + to_cmp + '.exe'
    std_exe = './' + std + '.exe'
    while run_set <= number_of_runs:
        input_io = IO("test.in", "test.out")
        if Config.version.split('.')[0] == '1':
            input_io.input_write(Config.generator(Config.data_set))
        else:
            ret = Config.Gen.generator(Config.data_set, input_io)
            if ret is not None:
                input_io.input_write(ret)
        try:
            Compare.program(
                to_cmp_exe, input=input_io, std_program=std_exe
            )
        except KeyboardInterrupt:
            print('Interrupted')
            break
        except compare.CompareMismatch:
            print(f"Wrong answer on testcase {run_set}")
            print('See input in ./test.in')
            break
        print(f'Passed set {run_set}')
        run_set += 1


if __name__ == '__main__':
    main()
