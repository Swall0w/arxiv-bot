#!usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="arxivbot",
    version="0.1.0",
    description="Create Issues about arxiv papers",
    url="https://github.com/Swall0w/arxiv-bot",
    license=license,
    packages=find_packages(exclude=('tests')),
    test_suite='tests',
    entry_points="""
    [console_scripts]
    pig = pig.pig:main
    """,
    )
