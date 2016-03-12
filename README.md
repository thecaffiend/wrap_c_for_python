# Examples of wrapping C headers (only headers with defines and structs) for use in python.
I needed to look at various tech for this purpose. These header files will
be wrapped for use in python to send/receive over a TCP socket for interaction
with a C application. Results of the research are here.

Each subfolder that names a tech (and has been implemented) produces an
extension module. They are built in place for testing purposes, and not as a
module for installation or distribution. The include directory contains the
common include files the extension modules operate on.

As of now, all of this was tested on Python 3.4 (via anaconda environments)
*except* for ctypesgen (which didn't work with python 3, and I used python
2.7). I may not have the dependencies quite up to date for each. I'll try to
update those as I go.

## Implemented

### ctypesgen

### cython

### swig

#### Dependencies
* Swig needs to be installed. This was tested using swig3.0
* Python is also needed. This is built for python3.

#### To build
* cd into the swig directory and run the build_ext.sh script
* NOTE: If the command to run swig is not `/usr/bin/swig3.0` the script will
   need to be modified to point to your swig executable.
* This will build the module in place

#### To test
* from the swig directory, run `python test_wrapper.py` to test the build.

#### To clean
* from the swig directory, run `rmbuilt.sh` to remove the built files

#### Findings

##### Pro
* Very easy to use (for this case)
* no dependencies (other than swig)
* good/large community
* distutils knows how to deal with it (swig can be run from setup.py)

##### Con
* gross generated code
* little control of the generated stuff. (e.g. char string max len 32 throws
  a TypeError if len exceeded. rather than truncating the str at max len here,
  it has to be handled elsewhere, like in a wrapper class)

## To come (maybe)
* pybindgen
* cffi
* xdress

## TODO
* do cffi and pybindgen, xdress examples
* add example usage scripts for each built Extension
* move findings and dependencies into README.md, with more detail
* look at making actual tests instead of simple asserts
* add example wrapper classes to illustrate functionality for sending/receiving
  over sockets.
