#!/usr/bin/env python

import header_wrapper as h

## TEST MH_LIST_ITEM_t ##

li = h.MH_LIST_ITEM_t()

# test the base values
print("Testing base values for MH_LIST_ITEM_t...")
try:
    assert li.itemType == 0
    assert li.scMsgType == 0
    assert li.nameStr == ''
except AssertationError:
    print('\tOne of the base value assertations failed.')
    exit()
print("SUCCESS - Test base values for MH_LIST_ITEM_t")

# set some values and test again
print("Setting values for MH_LIST_ITEM_t and testing those...")
try:
    li.itemType = 1
    li.scMsgType = 2
    li.nameStr = 'name'

    assert li.itemType == 1
    assert li.scMsgType == 2
    assert li.nameStr == 'name'
except AssertationError:
    print('\tOne of the set value assertations failed.')
    exit()
print("SUCCESS - Test set values for MH_LIST_ITEM_t")

# test the length constraint of the nameStr
print(
    "Testing MH_LIST_ITEM_t nameStr length constraint of %s" %
    h.MH_MAX_NAME_LEN
)
try:
    # this is 40 chars
    li.nameStr = ''.join(['name' for x in range(10)])
except TypeError:
    print('\tTypeError caught on name too long. Good')
else:
    print('\tFAILURE - TypeError *NOT* caught on name too long. Bad')
    exit()
print("SUCCESS - Test MH_LIST_ITEM_t nameStr length constraint.")


print("All tests succeeded!")
