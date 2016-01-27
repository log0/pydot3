#!/usr/bin/env python

import sys
from setuptools import setup

import os

os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

version = "1.0.8"

config = dict(
    name = 'pydot3',
    packages = ['pydot'],
    version = version,
    description = 'Python 3 interface to Graphviz\'s Dot',
    author = 'Eric Chio',
    author_email = 'ckieric@gmail.com',
    url = 'http://www.github.com/log0/pydot3/',
    download_url = 'https://github.com/log0/pydot3/archive/%s.zip' % version,
    license = 'MIT',
    keywords = 'graphviz dot graphs visualization pydot',
    platforms = ['any'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    install_requires = ['pyparsing', 'setuptools'],
    data_files = [('.', ['LICENSE', 'README.md'])])


if sys.version_info >= (3,):
    config.update(dict(
        use_2to3=True,
    ))

setup(**config)
