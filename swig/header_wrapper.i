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

%extend __mh_item_list_s
{
    /*
        TODO: How to use #defines from mainheader.h file here instead of 32?
    */
    inline size_t __len__() const {return $self->header.length;}

    /*
    Note: this makes the __mh_item_list_s struct itself have these methods.
          that means an object of the struct wrapper is indexed to get the
          values from the itemList. Which is weird. More reason for a sane
          wrapper class...
    */
    inline const struct __mh_list_item_s* __getitem__(int index)
    {
        if(index < 0 || index >= 64)
            return 0;
        return $self->itemList+(sizeof(struct __mh_list_item_s) * index);
    };

    void __setitem__(int index, const struct __mh_list_item_s* value)
    {
        if(index < 0 || index >= 64)
            return;
        $self->itemList[index] = *value;
    };
};
