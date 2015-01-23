# -*- encoding:utf-8 -*-
from __future__ import print_function
import io

from setuptools import setup


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.rst')

setup(
    name='logentries-cli',
    version='1.0',
    description='Get your logs from Logentries on the comandline',
    author='Adam Johnson',
    author_email='me@adamj.eu',
    url='http://github.com/adamchainz/logentries-cli/',
    license='GPLv3',
    install_requires=[
        'parsedatetime>=1.4',
        'python-dateutil>=2.4.0',
        'requests>=2.5.1',
    ],
    scripts=['bin/logentries'],
    long_description=long_description,
    packages=[],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: System :: Logging',
    ],
)
