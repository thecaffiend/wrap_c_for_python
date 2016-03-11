#!/usr/bin/env bash

WRAP_DIR=./swig_wrapper
GEN_SRC_DIR=${WRAP_DIR}/swig_gen_src
GEN_SRC_FILE=${GEN_SRC_DIR}/_header_wrapper.c
INC_DIRS=../include
FLAGS="-python -I${INC_DIRS} -outdir ${WRAP_DIR} -o ${GEN_SRC_FILE}"
IFACE_FILE=header_wrapper.i

# if a 'swig_generated' directory exists in the swig_wrapper dir, nuke it
echo "Nuking previous generated source dir (${GEN_SRC_DIR})"
rm -rf ${GEN_SRC_DIR}

#now make a clean dir for the generated files
echo "Making new generated source dir (${GEN_SRC_DIR})"
mkdir ${GEN_SRC_DIR}

# generate the things...
echo "Running swig on ${IFACE_FILE}..."
swig3.0 ${FLAGS} ${IFACE_FILE}
