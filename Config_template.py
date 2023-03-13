# encoding: utf-8

# version 2 Config Template
from cyaron import *
from libs.glib import ToolSet

# Constant Definitions
version = '2.0.0'
std_name = 'std.cpp'
data_set = 20

# Experimental Function
no_gen = False
genOut = False  # Generate Output in Gen.generator


# Gen class
class Gen:
    class static:
        # static vars
        pass

    class functions:
        # functions
        pass

    # gen.generator:
    #  param: data_group -> which data is being generated
    #  directly write input data to io
    #  See https://github.com/luogu-dev/cyaron/wiki/输入输出-IO
    @staticmethod
    def generator(data_group: int, io: IO) -> None:
        pass
