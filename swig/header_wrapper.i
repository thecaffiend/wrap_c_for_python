%module header_wrapper

%include "stdint.i"

%{
#define SWIG_FILE_WITH_INIT
#include <stdint.h>
#include "syscommon.h"
#include "mainheader.h"
%}
%include "syscommon.h"
%include "mainheader.h"
