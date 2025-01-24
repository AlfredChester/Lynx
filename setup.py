# !/usr/bin/env python
from setuptools import setup, find_packages
from Lynx.utils.constants import VERSION

packages = find_packages()

# CPP templates
packages += [
    "Lynx.templates",
    "Lynx.templates.cpp",
    "Lynx.templates.cpp.programs",
    "Lynx.templates.cpp.testdata",
    "Lynx.templates.cpp.additional_file",
]

# testlib
packages += ["testlib", "testlib.checkers", "testlib.validators"]

setup(
    name="pyLynx",
    version=VERSION,
    keywords="olympic informatics testcase testcase-tools tools",
    description="lynx: Next generation high performance testcase tool set for OI / ACM contests. - 新一代信息学竞赛数据生成工具集",
    license="MIT",
    py_modules=["Lynx"],
    author="AlfredChester",
    author_email="fredbao1126@gmail.com",
    packages=packages,
    include_package_data=True,
    platforms="any",
    install_requires=["Click", "cyaron", "tqdm", "PyYAML"],
    entry_points="""
        [console_scripts]
        lynx=Lynx:cli
    """,
)
