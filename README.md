# Testdata-Generator

A testdata generator and comparer repository powered by
`<a href="https://github.com/luogu-dev/cyaron/">`Cyaron`</a>`

### 1. Testdata Generator

First, you need to create a folder to save all the files needed for a problem, for example, I created `generator_example\`

Next, you need two files: `Config.py` and `std.cpp`

You need to place them like that:

```
generator_example\
  |- Config.py
  |- std.cpp
```

In `Config.py`, you need to rewrite the method `Gen.generator`, It should do one of the two things:

    1) Return a str with testdata, for example:

```python
from cyaron import *
class Gen:
    @staticmethod
    def generator(data_group: int, io: IO) -> str: 
        return '114514'
```

    2) Write testdata to io (which is recommended), for example:

```python
from cyaron import *
from libs.glib import ToolSet

class Gen:
    @staticmethod
    def generator(data_group: int, io: IO) -> None: 
        a = randint(ToolSet.INT_MIN, ToolSet.INT_MAX)
        b = randint(ToolSet.INT_MIN, ToolSet.INT_MAX)
        io.input_writeln(a, b)
```

In `std.cpp`, you just need to write a standard program which can solve the problem

**You don't need to redirect stdin or stdout**

It is optional to have a directory with no `std.cpp` inside and enables `genOut` which is still an experimental function

Then, run the command `python general.py {folder_name}`

Finally, the testdata will be auto generated and zipped, the folder will be looked like:

```
generator_example\
  |- Config.py
  |- std.cpp
  |- std.exe
  |- 1.in
  |- 1.out
  |- 2.in
  |- 2.out
  | ....
  |- generator_example.zip
```

### 2. Comparer

Using the comparer, you can compare the two programs
