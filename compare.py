from sys import argv
from os import system
from importlib import import_module

from cyaron import *

print('Usage: python compare.py {Data Generator} {program1} {program2}')
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
    std    = argv[3]
    print(f"To_cmp: {to_cmp}, std: {std}")
except:
    print("To_cmp or std lost, compare terminated")
    exit(0)

print('Problem Root:', root)
moduleRoot = root.replace('/', '.')
try:
    Config = import_module(moduleRoot + '.Config')
except Exception:
    print('No Config.py found, please check the directory')
    exit(0)

print('Read Config v' + Config.version)

def compileCpp(name : str) -> int:
    cmd = f"g++ -O3 -g -m64 -std=c++14 -Wall -o {name}.exe {name}"
    print("Compile cmd: ", cmd)
    return system(cmd)

def main() -> int:
    compileCpp(to_cmp)
    compileCpp(std)
    to_cmp_exe = './' + to_cmp + '.exe'
    std_exe = './' + std + '.exe'
    run_set = 1
    while True:
        input_io = IO("test.in", "test.out")
        if Config.version.split('.')[0] == '1':
            input_io.input_write(Config.generator(Config.data_set))
        else:
            ret = Config.Gen.generator(Config.data_set, input_io)
            if ret != None:
                input_io.input_write(ret)
        try:
            Compare.program(
                to_cmp_exe, input = input_io, std_program = std_exe
            )
        except KeyboardInterrupt:
            print('Interrupted')
            break
        except:
            print(f"Wrong answer on testcase {run_set}")
            print('See input in ./test.in')
            break
        print(f'Passed set {run_set}')
        run_set += 1
    
if __name__ == '__main__':
    main()
