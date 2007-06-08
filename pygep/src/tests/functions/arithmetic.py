from pygep.functions.math.arithmetic import add_op, subtract_op, multiply_op, divide_op
from pygep.functions.math.power import power_op, root_op
import unittest


class ArithmeticTest(unittest.TestCase):
    '''Tests the arithmetic non-terminals'''
    def testBasic(self):
        self.assertEqual(5, add_op(2, 3))
        self.assertEqual(-5, subtract_op(5, 10))
        self.assertEqual(10, multiply_op(2, 5))
        self.assertEqual(2, divide_op(4, 2))


    def testExtended(self):
        self.assertEqual(8, power_op(2,3))
        self.assertEqual(5, root_op(25))


    def testErrors(self):
        self.assertRaises(ZeroDivisionError, divide_op, 1, 0)
        self.assertRaises(ValueError, root_op, -1)


if __name__ == '__main__':
    unittest.main()
