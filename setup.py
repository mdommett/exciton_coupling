#!/usr/bin/env python

from distutils.core import setup

setup(name='exciton_coupling',
      version='0.1',
      description='Exciton coupling analysis',
      long_description=open('README.md').read(),
      author='Michael Dommett, Rachel Crespo-Otero',
      author_email='m.dommett@qmul.ac.uk',
      install_requires=[
        'periodic'],
      packages=['exciton_coupling',
                'exciton_coupling.utils'])
