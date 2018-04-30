# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

from setuptools import setup

REQUIRES = [
    'tornado>=3.11',
    'botframework-connector>=4.0.0.a2']

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'simple_bot', 'about.py')) as f:
    package_info = {}
    info = f.read()
    exec(info, package_info)

setup(
    name='simple_bot',
    version=package_info['__version__'],
    url=package_info['__uri__'],
    author=package_info['__author__'],
    description=package_info['__description__'],
    keywords=['bots', 'ai', 'botframework'],
    long_description=package_info['__summary__'],
    license=package_info['__license__'],
    packages=['simple_bot', 'simple_bot.bot_type_handlers', 'simple_bot.tornado_handlers', 'simple_bot.util'],
    install_requires=REQUIRES,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)
