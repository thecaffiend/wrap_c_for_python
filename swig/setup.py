#!/usr/bin/env python

"""
setup.py file for SWIG header_wrapper example
"""

from distutils.core import setup, Extension
import os.path

srcs = ['header_wrapper.i',]
inc_dirs = [os.path.abspath('../include'),]
inc_flags = list(map(lambda x: '-I%s' % x, inc_dirs))

# just need the include pathsat the moment...
swig_opts = []

swig_opts.extend(inc_flags)

header_wrapper_module = Extension('_header_wrapper',
                           sources=srcs,
                           swig_opts=swig_opts,
                           include_dirs=inc_dirs,
                        )

setup (name = 'header_wrapper',
       version = '0.1',
       author      = "thecaffiend",
       description = """Swig test for header_wrapper""",
       ext_modules = [header_wrapper_module],
       py_modules = ["swig_wrapper"],
       )
