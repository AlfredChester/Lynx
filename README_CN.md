# Testcase-Tools

[English Readme](./README.md)

由[Cyaron](https://github.com/luogu-dev/cyaron/)提供支持的测试用例工具集

前期准备: 运行`pip install -r requirements.txt`

### 1. 测试用例生成器

首先，您需要创建一个文件夹来保存问题所需的所有文件，例如，我创建了 `generator_example\`

接下来，您需要两个文件：`Config.py`和 `std.cpp`

你需要这样放置它们：

```
generator_example\
  |- Config.py
  |- std.cpp
```

在 `Config.py`中，您需要重写方法 `Gen.generator`，它应该做以下两件事之一：

1) 返回测试用例输入的str，例如：

```python
from cyaron import *
class Gen:
    @staticmethod
    def generator(data_group: int, io: IO) -> str: 
        return '114514'
```

2) 将测试用例数据写入 `io`（推荐使用），例如：

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

在 `std.cpp`中，您只需要编写一个可以解决问题的标准程序

**您不需要重定向stdin或stdout**

内部没有 `std.cpp`的目录是可选的，你可以在 `Config.py`中将 `genOut`设置为True，并且在 `Gen.generator`中写上输出，但是这仍然是一个实验性功能

然后，运行命令 `python general.py｛folder_name｝`

最后，测试用例将自动生成并压缩，文件夹将如下所示：

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

### 2. 比较器

使用比较器，您可以用同一个数据比较两个cpp代码的输出

用法：``python compare.py {Data Generator} {program1} {program2} {(Optional) Number of runs}``

### 3. SPJ检查器

使用spj检查器，您可以spj您的std

用法：``python spj_checker.py {Data Generator} {spj_program} {tested_program} {(Optional) Number of runs}``
