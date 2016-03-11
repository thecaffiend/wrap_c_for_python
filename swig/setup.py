#!/usr/bin/env python

"""
setup.py file for SWIG header_wrapper example
"""

from distutils.core import setup, Extension


header_wrapper_module = Extension('_header_wrapper',
                           sources=['_header_wrapper.c',],
                           include_dirs = ['../include'],
                           )

setup (name = 'header_wrapper',
       version = '0.1',
       author      = "thecaffiend",
       description = """Swig test for header_wrapper""",
       ext_modules = [header_wrapper_module],
       py_modules = ["header_wrapper"],
       )
