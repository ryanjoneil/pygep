from pygep.functions.linkers import sum_linker
from tests.base import Computation
import unittest


class CrossoverTest(unittest.TestCase):
    def setUp(self):
        gen = Computation.generate(5, 3)
        self.chromosome1 = gen.next()
        self.chromosome2 = gen.next()


    def _verify(self, p1, p2, c1, c2):
        for i in xrange(len(c1)):
            self.assertTrue(c1[i] in [p1[i], p2[i]])
            self.assertTrue(c2[i] in [p1[i], p2[i]])
            self.assertEqual(p1[i]==p2[i], c1[i]==c2[i])


    def testCrossoverOnePoint(self):
        c1, c2 = self.chromosome1.crossover_one_point(self.chromosome2)
        self._verify(self.chromosome1, self.chromosome2, c1, c2)


    def testCrossoverTwoPoint(self):
        c1, c2 = self.chromosome1.crossover_two_point(self.chromosome2)
        self._verify(self.chromosome1, self.chromosome2, c1, c2)


    def testCrossoverGene(self):
        c1, c2 = self.chromosome1.crossover_gene(self.chromosome2)
        self._verify(self.chromosome1, self.chromosome2, c1, c2)


if __name__ == '__main__':
    unittest.main()
