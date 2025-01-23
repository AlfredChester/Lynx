import os
import shutil

from Lynx.utils.constants import *
from Lynx.utils.log import *

"""The structure of a problem directory is as follows:
.
├── {problem_path}
│   ├── problem.yaml
│   ├── problem_zh.md
│   ├── testdata
│   │   ├── config.yaml
│   │   ├── a1.in
│   │   └── a1.out
│   └── additional_file
│       ├── a.png
│       └── b.pdf
└── ...
"""


def init_problem(problem_path: str, standard: str, checker: str, validator: str):
    shutil.copytree(CPP_TEMPLATES_ROOT, problem_path)
    shutil.copyfile(
        os.path.join(TEMPLATES_ROOT, "generator.py"),
        os.path.join(problem_path, "programs", "generator.py"),
    )
    os.remove(os.path.join(problem_path, "additional_file", ".gitkeep"))
