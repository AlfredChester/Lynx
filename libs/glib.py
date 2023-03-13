from cyaron import *
from typing import *
from string import *


class ToolSet:
    INT_MAX = (1 << 31) - 1
    INT_MIN = -INT_MAX - 1
    general_mod = int(1e9 + 7)

    def genRandVector(io: IO, vec_len: int, data_range, allow_same=True):
        if isinstance(data_range, int):
            data_range = (0, data_range)
        to_write = Vector.random(vec_len, [data_range], int(allow_same))
        for item in to_write:
            io.input_write(item)
        io.input_writeln()

    def genRandStr(siz: int, gen_src=ascii_letters) -> str:
        ret = ''
        for _ in range(siz):
            ret += choice(gen_src)
        return ret
