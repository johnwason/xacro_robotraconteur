#!/usr/bin/env python

from setuptools import setup

setup(
    name="robotraconteur_xacro",
    version=0.1,
    license = "BSD",
    packages=['xacro_robotraconteur'],
    package_dir={'': 'src'},
    scripts=['scripts/xacro-robotraconteur']
)

