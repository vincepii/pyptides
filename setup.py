#!/usr/bin/env python

from distutils.core import setup

setup(name='tool-elena',
      version='0.1',
      description='Analyzes output of unknown tool',
      author='Vincenzo Pii',
      author_email='vinc.pii@gmail.com',
      url='',
      #packages=['distutils', 'distutils.command'],
      requires=['matplotlib', 'numexpr']
     )