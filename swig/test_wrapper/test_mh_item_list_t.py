import unittest
from header_wrapper import (
    MH_ITEM_LIST_t,
    MH_LIST_ITEM_t,
    SC_HEADER_t,
)

class MhItemListTTest(unittest.TestCase):
    """
    Test the SC_HEADER_t wrapper class.
    """

    def setUp(self):
        """Setup for the tests"""
        print('MhItemListTTest:setUp_:begin')
        l = [MH_LIST_ITEM_t() for i in range(2)]
        self.mil_base = MH_ITEM_LIST_t()
        self.mil_set = MH_ITEM_LIST_t()
        self.mil_set.header.type = 1
        self.mil_set.header.status = 2
        self.mil_set.header.code = 3
        self.mil_set.header.length = len(l)
        for i in range(len(l)):
            l[i].itemType = i+1
            l[i].scMsgType = i+2
            l[i].nameStr = 'name%s' % i
            # this sets the value of the object at index in
            # self.mil_set.itemList to l[i]
            self.mil_set[i] = l[i]
        print('MhItemListTTest:setUp_:end')

    def tearDown(self):
        """No teardown needed here..."""
        print ('MhItemListTTest:tearDown_:begin')
        print ('MhItemListTTest:tearDown_:end')

    def testBaseValues(self):
        """Test the default values of the wrapper"""
        print ('MhItemListTTest:testBaseValues')
        self.assertEqual(self.mil_base.header.type, 0)
        self.assertEqual(self.mil_base.header.status, 0)
        self.assertEqual(self.mil_base.header.code, 0)
        self.assertEqual(self.mil_base.header.length, 0)
        # this tests the legth of the itemList member, not the length of the
        # wrapped struct. See the swig interface file
        self.assertEqual(len(self.mil_base), 0)

    def testSetValues(self):
        """Test the values in the mil_set are set correctly"""
        print ('MhItemListTTest:testSetValues')
        self.assertEqual(self.mil_set.header.type, 1)
        self.assertEqual(self.mil_set.header.status, 2)
        self.assertEqual(self.mil_set.header.code, 3)
        self.assertEqual(self.mil_set.header.length, 2)
        # this tests the legth of the itemList member, not the length of the
        # wrapped struct. See the swig interface file
        self.assertEqual(len(self.mil_set), self.mil_set.header.length)
