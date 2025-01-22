# !/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="lynx",
    version="2.0.1-beta",
    keywords="olympic informatics testcase testcase-tools tools",
    description="lynx: Next generation high performance testcase tool set for OI / ACM contests. - 新一代信息学竞赛数据生成工具集",
    license="MIT",
    py_modules=["Lynx"],
    author="AlfredChester",
    author_email="fredbao1126@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["Click", "cyaron", "tqdm"],
    entry_points="""
        [console_scripts]
        lynx=Lynx:cli
    """,
)
