#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup,find_packages

setup(
    name = "demo",
    version = "0.2",
    url = "https://github.com/untrunk/Demo.git",
    long_description = open('README.md').read(),
    packages = find_packages(),
)
