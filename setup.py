#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="testcase-tools",
    version="2.0.0-beta",
    keywords="olympic informatics testcase testcase-tools tools",
    description="Testcase-tools: Next generation high performance testcase tool set for OI / ACM contests. - 新一代信息学竞赛数据生成工具集",
    license="MIT",
    author="ABOJ Development Team",
    author_email="abonlinejudge@163.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["fire", "cyaron", "tqdm"],
)
