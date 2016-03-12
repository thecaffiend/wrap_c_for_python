import unittest
from header_wrapper import (
    SC_HEADER_t,
)

class ScHeaderTTest(unittest.TestCase):
    """
    Test the SC_HEADER_t wrapper class.
    """

    def setUp(self):
        """Setup for the tests"""
        print("ScHeaderTTest:setUp_:begin")
        self.sch = SC_HEADER_t()
        print("ScHeaderTTest:setUp_:end")

    def tearDown(self):
        """No teardown needed here..."""
        print ("ScHeaderTTest:tearDown_:begin")
        print ("ScHeaderTTest:tearDown_:end")

    def testBaseValues(self):
        """Test the default values of the wrapper"""
        print ("ScHeaderTTest:testBaseValues")
        self.assertEqual(self.sch.type, 0)
        self.assertEqual(self.sch.status, 0)
        self.assertEqual(self.sch.code, 0)
        self.assertEqual(self.sch.length, 0)

    def testSetValues(self):
        """Set values and test they are set correctly"""
        print ("ScHeaderTTest:testSetValues")
        self.sch.type = 1
        self.sch.status = 2
        self.sch.code = 3
        self.sch.length = 4

        self.assertEqual(self.sch.type, 1)
        self.assertEqual(self.sch.status, 2)
        self.assertEqual(self.sch.code, 3)
        self.assertEqual(self.sch.length, 4)
