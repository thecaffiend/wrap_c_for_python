#!/usr/bin/env bash

# clone the repo for ctypesgen (a fork of the main that fixes a couple of
# things).
git clone https://github.com/r-ku/ctypesgen.git
# tested with this commit...
git checkout b5fd04293641ea773e2350d0b1c764dddf527c9c

# set the python path for the new repo's contents.
PYTHONPATH="./ctypesgen/ctypesgencore:./ctypesgen/ctypesgencore/processor:./ctypesgen/ctypesgencore/parser:./ctypesgen/ctypesgencore/printer_json:"

# this requires python2. hopefully this gets it. may need to change to match
# your setup. definitely so if not on *nix
/usr/bin/env python2 ./ctypesgen/ctypesgen.py ../include/*.h -o header_wrapper.py
