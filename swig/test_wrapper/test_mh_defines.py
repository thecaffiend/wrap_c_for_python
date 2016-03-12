import unittest
from header_wrapper import (
    MH_MAX_ITEMS,
    MH_MAX_NAME_LEN,
)

class MhDefinesTest(unittest.TestCase):
    """
    Test the #defines from the mainheader wrapper.
    """
    def testDefines(self):
        """Test the #define values of the wrapper"""
        print ('MhDefinesTest:testDefines')
        self.assertEqual(MH_MAX_ITEMS, 64)
        self.assertEqual(MH_MAX_NAME_LEN, 32)
