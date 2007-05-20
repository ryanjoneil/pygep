from pygep.functions.comparison import *
import unittest


class ComparisonTest(unittest.TestCase):
    '''Tests the comparison non-terminals'''
    def testEqual(self):
        self.assertEqual(1, equal(1, 1))
        self.assertEqual(2, equal(1, 2))


    def testUnequal(self):
        self.assertEqual(1, unequal(1, 2))
        self.assertEqual(2, unequal(2, 2))


    def testLess(self):
        self.assertEqual(1, less(1, 2))
        self.assertEqual(2, less(3, 2))


    def testGreater(self):
        self.assertEqual(2, greater(1, 2))
        self.assertEqual(3, greater(3, 2))


    def testLessOrEqual(self):
        self.assertEqual(1, less_or_equal(1,2))
        self.assertEqual(1, less_or_equal(1,1))
        self.assertEqual(2, less_or_equal(3,2))


    def testGreaterOrEqual(self):
        self.assertEqual(2, greater_or_equal(2,1))
        self.assertEqual(2, greater_or_equal(2,2))
        self.assertEqual(3, greater_or_equal(2,3))


if __name__ == '__main__':
    unittest.main()

