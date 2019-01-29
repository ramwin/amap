#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2018-07-04 10:37:16

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_pkg",
    version="0.0.1",
    author="Xiang Wang",
    author_email="ramwin@qq.com",
    description="python api for amap 高德地图的api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ramwin/amap",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
