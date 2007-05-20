from pygep.functions.linkers import *
import unittest


class LinkersTest(unittest.TestCase):
    '''Tests the sub-ET function linkers'''
    def testDefaultLinker(self):
        self.assertEqual(5, default_linker(5))
        self.assertEqual((5,6,7), default_linker(5,6,7))
    
    
    def testSumLinker(self):
        self.assertEqual(10, sum_linker(1,2,3,4))
    
    
    def testOrLinker(self):
        self.assertFalse(or_linker(False, 0, '', (), []))
        self.assertTrue(or_linker(0, 0, 1))


if __name__ == '__main__':
    unittest.main()
