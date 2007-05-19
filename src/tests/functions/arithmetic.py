from pygep.functions.arithmetic import *
import unittest


class ArithmeticTest(unittest.TestCase):
    '''Tests the arithmetic non-terminals'''
    def testBasic(self):
        self.assertEqual(5, add(2, 3))
        self.assertEqual(-5, subtract(5, 10))
        self.assertEqual(10, multiply(2, 5))
        self.assertEqual(2, divide(4, 2))


    def testExtended(self):
        self.assertEqual(8, power(2,3))
        self.assertEqual(5, root(25))


    def testErrors(self):
        self.assertRaises(ZeroDivisionError, divide, 1, 0)
        self.assertRaises(ValueError, root, -1)


if __name__ == '__main__':
    unittest.main()

