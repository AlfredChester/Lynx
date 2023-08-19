# encoding: utf-8

# version 2 Config Template
from cyaron import *
from typing import *
from string import *

# Constant Definitions
version = '2.2.0'
data_set = 20
std_name = 'std.cpp'
validator = 'validator.cpp'
cmd = 'g++ -O3 -g -m64 -std=c++14 -Wall -o {}/std.exe {}'

# Experimental Function
no_gen = False
genOut = False    # Generate Output in Gen.generator

# Tool Set


class ToolSet:
    general_mod = int(1e9 + 7)

    def genRandVector(io: IO, len, data_range, allow_same=True):
        if isinstance(data_range, int):
            data_range = (0, data_range)
        to_write = Vector.random(len, [data_range], int(allow_same))
        for item in to_write:
            io.input_write(item)
        io.input_writeln()

    def genRandStr(siz: int, gen_src=ascii_letters) -> str:
        ret = ''
        for _ in range(siz):
            ret += choice(gen_src)
        return ret


class Gen:
    class static:
        # static vars
        pass

    class functions:
        # functions
        pass

    def generator(data_group: int, io: IO) -> Optional[str]:  ...
