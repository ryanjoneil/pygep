from tests.base import Computation
import unittest


class InversionTest(unittest.TestCase):
    def testShortInversion(self):
        # 5: Makes sure inversion works with head length=1
        i = Computation.generate(1, 1).next()
        self.assertEqual(i, i.invert())

    
    def testNormalInversion(self):
        x = Computation.generate(2, 1).next()
        y = x.invert()
        
        # Heads should be switched, tails unaffected
        self.assertEqual(x.genes[0][2:], y.genes[0][2:])
        self.assertEqual(x.genes[0][0],  y.genes[0][1])
        self.assertEqual(x.genes[0][1],  y.genes[0][0])


if __name__ == '__main__':
    unittest.main()
