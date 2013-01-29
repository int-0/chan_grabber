#!/usr/bin/python
# -*- coding:utf-8; mode:python -*-

from distutils.core import setup

setup(name='chan-grabber',
      version='1.0',
      description='API from popular chan board to grab all images.',
      author='Tobías Díaz Díaz-Chirón',
      author_email='tobias.deb@gmail.com',
      packages=['chan'],
      scripts=['scripts/chan_grabber']
     )
