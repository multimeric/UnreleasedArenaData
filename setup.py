#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name='arena-data',
    packages=find_packages(exclude="test"),
    install_requires=[
        "scrython"
    ],
    entry_points={"console_scripts": ["arena-data=arena_data.cli:main"]},
)
