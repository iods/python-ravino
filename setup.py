#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Project:   python-ravino
# Copyright: (c) 2021, Rye Miller

"""The Ravino Blockchain."""

from setuptools import setup, find_packages

with open('README.md') as f:
    readme_file = f.read()

with open('LICENSE') as f:
    license_file = f.read()

setup(
    name='python-ravino',
    version='0.1.0',
    description='A blockchain experiment.',
    long_description=readme_file,
    author='Rye Miller',
    author_email='rye@drkstr.dev',
    url='https://github.com/iods/python-ravino',
    license=license_file,
    packages=find_packages(exclude=('tests', 'docs'))
)