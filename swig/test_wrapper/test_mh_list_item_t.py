import unittest
from header_wrapper import (
    MH_LIST_ITEM_t,
    MH_MAX_NAME_LEN,
)

class MhListItemTTest(unittest.TestCase):
    """
    Test the MH_LIST_ITEM_t wrapper class.
    """

    def setUp(self):
        """Setup for the tests"""
        print('MhListItemTTest:setUp_:begin')
        self.mli = MH_LIST_ITEM_t()
        print('MhListItemTTest:setUp_:end')

    def tearDown(self):
        """No teardown needed here..."""
        print ('MhListItemTTest:tearDown_:begin')
        print ('MhListItemTTest:tearDown_:end')

    def testBaseValues(self):
        """Test the default values of the wrapper"""
        print ('MhListItemTTest:testBaseValues')
        self.assertEqual(self.mli.itemType, 0)
        self.assertEqual(self.mli.scMsgType, 0)
        self.assertEqual(self.mli.nameStr, '')

    def testSetValues(self):
        """Set values and test they are set correctly"""
        print ('MhListItemTTest:testSetValues')
        self.mli.itemType = 1
        self.mli.scMsgType = 2
        self.mli.nameStr = 'steve'

        self.assertEqual(self.mli.itemType, 1)
        self.assertEqual(self.mli.scMsgType, 2)
        self.assertEqual(self.mli.nameStr, 'steve')

    def testNameLenConstraint(self):
        """Set the name to a long string to test the length constraint"""
        print ('MhListItemTTest:testNameLenConstraint')

        with self.assertRaises(TypeError):
            self.mli.nameStr = 's' * (MH_MAX_NAME_LEN+1)
