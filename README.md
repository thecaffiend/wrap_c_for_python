# Examples of wrapping C headers (only headers with defines and structs) for use in python.
I needed to look at various tech for this purpose. Results are here. Each
subfolder that names a tech (and has been implemented) produces an extension
module.

As of now, all of this was tested on Python 3.4 (via anaconda environments)
*except* for ctypesgen (which didn't work with python 3, and I used python
2.7). I may not have the dependencies quite up to date for each.

## Implemented
### ctypesgen
### cython
### swig
* Swig needs to be installed. This was tested using swig3.0
* To build this, cd into the swig directory and run the build_ext.sh script
 * If the command to run swig is not `/usr/bin/swig3.0` the script will need to
   be modified to point to your swig executable.
 * This will build the module in place (not as a proper module to be installed)
* run `python test_wrapper.py` to test the build. This was tested on python3.0
* run `rmbuilt.sh` to remove the built files

## To come (maybe)
* pybindgen
* cffi
* xdress

## TODO
* do cffi and pybindgen, xdress examples
* add example usage scripts for each built Extension
* move findings into root level file (perhaps in readme.md), with more detail
* look at making actual tests instead of simple asserts
