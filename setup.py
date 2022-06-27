#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
      long_description = f.read()

setup(name='pipelinewise-tap-snowflake',
      version='2.0.3',
      description='Singer.io tap for extracting data from Snowflake - PipelineWise compatible',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="TransferWise",
      url='https://github.com/transferwise/pipelinewise-tap-snowflake',
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3 :: Only'
      ],
      py_modules=['tap_snowflake'],
      install_requires=[
            'pipelinewise-singer-python==1.*',
            'snowflake-connector-python[pandas]==2.7.9',
            'pendulum==1.2.0',
            'python-dateutil>=2.1,<2.8.2'
      ],
      extras_require={
          'test': [
            'nose==1.3.7',
            'pylint==2.6.0',
            'unify==0.5'
          ]
      },
      entry_points='''
          [console_scripts]
          tap-snowflake=tap_snowflake:main
      ''',
      packages=['tap_snowflake', 'tap_snowflake.sync_strategies'],
)
