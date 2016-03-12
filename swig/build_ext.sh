#!/usr/bin/env bash

# path to swig executable. change this to match yours
SWIG_EXE=/usr/bin/swig3.0

# see if SWIG_EXE exists. if not, prompt the user
${SWIG_EXE} -version >> /dev/null
if [ $? -eq 0 ]; then
    echo "Seems swig is available, trying to build the extension..."
else
    echo "The swig executable specified in this script is not available."
    echo "If swig is installed, change the executable path in this script"
    exit 1
fi

echo "Building extension..."
echo "Running: python ./setup.py build_ext --swig ${SWIG_EXE}"
python ./setup.py build_ext --swig ${SWIG_EXE} --inplace
