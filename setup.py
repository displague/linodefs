#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='linodefs',
    version='0.1',
    description='FUSE-based filesystem for accessing Linode resources',
    long_description=open('README.md').read(),
    author='Marques Johansson',
    author_email='marques@displague.com',
    url='https://github.com/displague/linodefs',
    license='MIT',
    packages=find_packages(),
    install_requires=['future'],
    scripts=['linodefs.py',],
    classifiers=[
      'Development Status :: 1 - Planning',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Topic :: System :: Filesystems',
      ]
    )

