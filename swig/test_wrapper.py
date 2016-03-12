#!/usr/bin/env python

# TODO: CLEAN THIS UP! THE EYES, THEY BURN
import header_wrapper as h

# indices
DEFAULT = 0
SETVAL = 1

def print_msg(s, indent=0):
    """
    """
    indstr = ''.join(['\t' for i in range(indent)])
    print(indstr+s)

def test_fields(obj, fld_spec, test_setval=False):
    """
    """
    for k, v in fld_spec.items():
        # there has to be a better way to do this than 2 try catches
        try:
            getattr(obj, k)
            print_msg("SUCCESS: field %s exists" % (k), indent=2)
        except AttributeError:
            print_msg("FAILURE: field %s does not exist" % (k), indent=2)
            continue

        idx = SETVAL if test_setval else DEFAULT
        try:
            assert getattr(obj, k) == v[idx]
            print_msg(
                "SUCCESS: %s value %s matches expected %s" % (
                    k,
                    getattr(obj, k),
                    v[idx],
                ),
                indent=2
            )
        except AssertionError:
            print_msg(
                "FAILURE: %s value %s does not match expected %s" % (
                    k,
                    getattr(obj, k),
                    v[idx],
                ),
                indent=2
            )

def set_fields(obj, fld_spec):
    """
    """
    #TODO: error check here
    for k, v in fld_spec.items():
        setattr(obj, k, v[SETVAL])
    return obj

#######################
## syscommon.h tests ##
#######################
print_msg("Testing syscommon.h wrappers...")

## TEST SC_HEADER_t ##
sch = h.SC_HEADER_t()
sch_flds = {
    'type': [0, 1],
    'status': [0, 2],
    'code': [0, 3],
    'length': [0, 4],
}

# test the base values
print_msg("Testing base values for SC_HEADER_t...", indent=1)
test_fields(sch, sch_flds)
obj=set_fields(sch, sch_flds)
test_fields(sch, sch_flds, test_setval=True)
# try:
#     assert sch.type == 0
#     assert sch.status == 0
#     assert sch.code == 0
#     assert sch.length == 0
# except AssertationError:
#     print('\t\tOne of the base value assertations failed.')
#     exit()
print_msg("SUCCESS - Test base values for SC_HEADER_t", indent=1)

# set some values and test again
print("\tSetting values for SC_HEADER_t and testing those...")
try:
    sch.type = 1
    sch.status = 2
    sch.code = 3
    sch.length = 4

    assert sch.type == 1
    assert sch.status == 2
    assert sch.code == 3
    assert sch.length == 4
except AssertationError:
    print('\t\tOne of the set value assertations failed.')
    exit()
print("\tSUCCESS - Test set values for SC_HEADER_t")

########################
## mainheader.h tests ##
########################
print("Testing syscommon.h wrappers...")

## TEST MH_LIST_ITEM_t ##

li = h.MH_LIST_ITEM_t()

# test the base values
print("\tTesting base values for MH_LIST_ITEM_t...")
try:
    assert li.itemType == 0
    assert li.scMsgType == 0
    assert li.nameStr == ''
except AssertationError:
    print('\t\tOne of the base value assertations failed.')
    exit()
print("\tSUCCESS - Test base values for MH_LIST_ITEM_t")

# set some values and test again
print("\tSetting values for MH_LIST_ITEM_t and testing those...")
try:
    li.itemType = 1
    li.scMsgType = 2
    li.nameStr = 'name'

    assert li.itemType == 1
    assert li.scMsgType == 2
    assert li.nameStr == 'name'
except AssertationError:
    print('\t\tOne of the set value assertations failed.')
    exit()
print("\tSUCCESS - Test set values for MH_LIST_ITEM_t")

# test the length constraint of the nameStr
print(
    "\tTesting MH_LIST_ITEM_t nameStr length constraint of %s" %
    h.MH_MAX_NAME_LEN
)
try:
    # this is 40 chars
    li.nameStr = ''.join(['name' for x in range(10)])
except TypeError:
    print('\t\tTypeError caught on name too long. Good')
else:
    print('\t\tFAILURE - TypeError *NOT* caught on name too long. Bad')
    exit()
print("\tSUCCESS - Test MH_LIST_ITEM_t nameStr length constraint.")


print("All tests succeeded!")
