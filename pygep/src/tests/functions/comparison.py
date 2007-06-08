from pygep.functions.math.comparison import (equal_op, unequal_op, less_op, 
    greater_op, less_or_equal_op, greater_or_equal_op)
import unittest


class ComparisonTest(unittest.TestCase):
    '''Tests the comparison non-terminals'''
    def testEqual(self):
        self.assertEqual(1, equal_op(1, 1))
        self.assertEqual(2, equal_op(1, 2))


    def testUnequal(self):
        self.assertEqual(1, unequal_op(1, 2))
        self.assertEqual(2, unequal_op(2, 2))


    def testLess(self):
        self.assertEqual(1, less_op(1, 2))
        self.assertEqual(2, less_op(3, 2))


    def testGreater(self):
        self.assertEqual(2, greater_op(1, 2))
        self.assertEqual(3, greater_op(3, 2))


    def testLessOrEqual(self):
        self.assertEqual(1, less_or_equal_op(1,2))
        self.assertEqual(1, less_or_equal_op(1,1))
        self.assertEqual(2, less_or_equal_op(3,2))


    def testGreaterOrEqual(self):
        self.assertEqual(2, greater_or_equal_op(2,1))
        self.assertEqual(2, greater_or_equal_op(2,2))
        self.assertEqual(3, greater_or_equal_op(2,3))


if __name__ == '__main__':
    unittest.main()
