# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ml_trade',
    version='0.0.1',
    description='',
    long_description=readme,
    author='Kazumi Malhan',
    author_email='i7adler@gmail.com',
    install_requires=['numpy',
                      'pandas',
                      'pandas-datareader',
                      'datetime',
                      'matplotlib',
                      'pytest'],
    url='https://github.com/kmalhan/ml_trade',
    license=license,
    packages=find_packages(exclude=('tests','docs'))
)