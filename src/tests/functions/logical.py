from pygep.functions.logical import and_op, or_op, not_op, if_op
import unittest


class LogicTest(unittest.TestCase):
    '''Tests the logic non-terminals'''
    def testAnd(self):
        self.assertTrue(and_op(1, 1))
        self.assertFalse(and_op(1, 0))


    def testOr(self):
        self.assertTrue(or_op(1, 2))
        self.assertFalse(or_op(0, 0))


    def testNot(self):
        self.assertTrue(not_op(False))
        self.assertFalse(not_op(1))

    
    def testIf(self):
        self.assertEqual(1, if_op(True, 1, 2))
        self.assertEqual(2, if_op(False, 1, 2))


if __name__ == '__main__':
    unittest.main()
