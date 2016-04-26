# -*- coding: utf-8 -*-
# This file is part of fedmsg.
# Copyright (C) 2016 Elan Ruusamäe <glen@pld-linux.org>
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Elan Ruusamäe <glen@pld-linux.org>
#

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys

f = open('README.md')
long_description = f.read().strip()
f.close()

# Ridiculous as it may seem, we need to import multiprocessing and
# logging here in order to get tests to pass smoothly on python 2.7.
try:
    import multiprocessing
    import logging
except Exception:
    pass


install_requires = [
    'fedmsg',
    'python-dateutil',
    'pytz'
]
tests_require = [
    'nose',
]

if sys.version_info < (2, 7):
    install_requires.extend([
        'argparse',
        'ordereddict',
    ])
    tests_require.extend([
        'unittest2',
    ])

entry_points = {
    'fedmsg.meta': [
        "scm=fedmsg_meta_pld.scm:SCMProcessor",
    ]
}

setup(
    name='fedmsg_meta_pld',
    version='0.0.1',
    description="fedmsg metadata providers for PLD Linux",
    long_description=long_description,
    author='Elan Ruusamäe',
    author_email='glen@pld-linux.org',
    url='https://github.com/glensc/fedmsg_meta_pld/',
    license='LGPLv2+',
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='nose.collector',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points=entry_points
)
