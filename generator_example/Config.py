# encoding: utf-8

# version 2 Config Template
from cyaron    import *         # cyaron
from libs.glib import ToolSet   # Toolset

# Constant Definations
version  = '2.0.0'
std_name = 'std.cpp'
data_set = 10

# Experimental Function
no_gen   = False
genOut   = False    # Generate Output in Gen.generator

# Gen class
class Gen:
    class static:
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)
        pass

    class functions:
        # functions
        pass

    # gen.generator:
    #  param: data_group -> which data is being generated
    #  directly write input data to io
    #  See https://github.com/luogu-dev/cyaron/wiki/输入输出-IO
    def generator(data_group: int, io: IO) -> None:
        a = randint(Gen.static.INT_MIN, Gen.static.INT_MAX)
        b = randint(Gen.static.INT_MIN, Gen.static.INT_MAX)
        io.input_writeln(a, b)
