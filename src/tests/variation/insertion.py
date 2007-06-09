from tests.base import Computation
import unittest


class ISTranspositionTest(unittest.TestCase):
    def testShortIS(self):
        # 5: IS transposition should do nothing if head length=1
        i = Computation.generate(1, 1).next()
        self.assertEqual(i, i.transpose_is(1))


if __name__ == '__main__':
    unittest.main()
