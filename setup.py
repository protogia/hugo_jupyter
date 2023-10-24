#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from utils import get_packages_from_lockfile

from setuptools import setup

setup(
    install_requires=[
        "docopt",
        "fabric3",
        "watchdog",
        "jupyter",
        "colorama",
        "jupyter-contrib-nbextensions",
        "crayons",

        "bumpversion",
        "coverage",
        "cryptography",
        "flake8",
        "pytest",
        "pytest-runner",
        "pyyaml",
        "sphinx",
        "tox",
        "sphinx-autodoc-typehints",
        "wheel",
    ],
    entry_points={
        'console_scripts': [
            'hugo_jupyter=hugo_jupyter.cli:main'
        ]
    },

)
