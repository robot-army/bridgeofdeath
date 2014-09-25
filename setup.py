#! /usr/bin/python2.7 -OO
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'Bridgeofdeath',
    version = '0.0.1',
    description = 'RFID Door system',
    author = 'Barnaby Shearer',
    author_email = 'b@zi.is',
    license = "GNU GPLv2",
    url = 'https://zi.is/p/browser/bridgeofdeath',
    packages = [
        'pyfare',
        'models',
        'settings',
        'logger',
    ],
    scripts = [
        'bin/read_token.py',
        'bin/write_token.py',
    ],
    install_requires = [
        "pycrypto",
        "pyserial",
    ],
)
