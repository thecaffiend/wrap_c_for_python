#!/usr/bin/env python

import header_wrapper as h

li = h.MH_LIST_ITEM_t()

# test the base values
assert li.itemType == 0
assert li.scMsgType == 0
assert li.nameStr == ''
