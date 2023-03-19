from importlib import import_module
from os import system

from cyaron import *

from libs.glib import args as argv

print('Usage: python spj_checker.py {Data Generator} {spj_program} {tested_program}')
print(f'Argv: {argv}')
try:
    root = argv[1]
except IndexError:
    print("No Problem Id given, compare terminated")
    exit(0)

if root.startswith('.\\') or root.startswith('./'):
    root = root[2:]

try:
    spj = argv[2]
    to_test = argv[3]
    print(f"spj: {spj}, to_test: {to_test}")
except IndexError:
    print("spj or to_test lost, compare terminated")
    exit(0)

print('Problem Root:', root)
moduleRoot = root.replace('/', '.')
try:
    Config = import_module(moduleRoot + '.Config')
except FileNotFoundError:
    print('No Config.py found, please check the directory')
    exit(0)

print('Read Config v' + Config.version)

try:
    useConfigGen = Config.genOut
except AttributeError:
    useConfigGen = False

def compile_source(name: str) -> int:
    cmd = f"g++ -O3 -g -m64 -std=c++14 -Wall -o {name}.exe {name}"
    print("Compile cmd: ", cmd)
    return system(cmd)


def main(*args, **kwargs) -> int:
    run_set = 1
    compile_source(spj)
    compile_source(to_test)
    spj_exe = './' + spj + '.exe'
    to_test_exe = './' + to_test + '.exe'
    while True:
        input_io = IO("test.in", "test.out")
        if Config.version.split('.')[0] == '1':
            input_io.input_write(Config.generator(Config.data_set))
        else:
            ret = Config.Gen.generator(Config.data_set, input_io)
            if ret is not None:
                input_io.input_write(ret)
        if not useConfigGen:
            input_io.output_gen(to_test_exe)
        try:
            res = system(f'{spj_exe} test.in test.out')
            if res != 0:
                print(f'Wrong answer on set {run_set}')
                return
        except KeyboardInterrupt:
            print('Interrupted')
            break
        print(f'Passed set {run_set}')
        run_set += 1


if __name__ == '__main__':
    main()
