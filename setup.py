#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2024/3/30 18:30
Desc: AKShare's PYPI info file
"""

import ast
import re


import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


def get_version_string() -> str:
    """
    get the version of waizaowang
    :return: version number
    :rtype: str, e.g. '0.6.24'
    """
    with open("waizao/__init__.py", "rb") as _f:
        version_line = re.search(
            pattern=r"__version__\s+=\s+(.*)", string=_f.read().decode("utf-8")
        ).group(1)
        return str(ast.literal_eval(version_line))


setuptools.setup(
    name="waizao",
    version=get_version_string(),
    author="waizaowang",
    author_email="waizaowang@163.com",
    description="Simple financial data interface library for Python!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://waizaowang.com/",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas>=0.25",
        "requests>=2.22.0",
    ],
    package_data={"": ["*.py", "*.json", "*.pk", "*.js", "*.zip"]},
    keywords=[
        "waizao",
        "futures",
        "fund",
        "bond",
        "index",
        "finance",
        "spider",
        "quant",
        "quantitative",
        "investment",
        "trading",
        "data",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
