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
        print('ScHeaderTTest:setUp_:begin')
        self.sch_base = SC_HEADER_t()
        self.sch_set = SC_HEADER_t()
        self.sch_set.type = 1
        self.sch_set.status = 2
        self.sch_set.code = 3
        self.sch_set.length = 4


        print('ScHeaderTTest:setUp_:end')

    def tearDown(self):
        """No teardown needed here..."""
        print ('ScHeaderTTest:tearDown_:begin')
        print ('ScHeaderTTest:tearDown_:end')

    def testBaseValues(self):
        """Test the default values of the wrapper"""
        print ('ScHeaderTTest:testBaseValues')
        self.assertEqual(self.sch_base.type, 0)
        self.assertEqual(self.sch_base.status, 0)
        self.assertEqual(self.sch_base.code, 0)
        self.assertEqual(self.sch_base.length, 0)

    def testSetValues(self):
        """Set values and test they are set correctly"""
        print ('ScHeaderTTest:testSetValues')
        self.assertEqual(self.sch_set.type, 1)
        self.assertEqual(self.sch_set.status, 2)
        self.assertEqual(self.sch_set.code, 3)
        self.assertEqual(self.sch_set.length, 4)
