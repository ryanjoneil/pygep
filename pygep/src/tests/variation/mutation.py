from pygep.gene import KarvaGene
from tests.base import Computation
import unittest


def z(x, y):
    pass


class MutationTest(unittest.TestCase):
    '''Verifies effects of mutation per allele'''
    def setUp(self):
        self.gene = KarvaGene([z,z,'y',3,4], 1)
        self.chromosome = Computation([self.gene], 2)


    def testAllMutate(self):
        newchr = self.chromosome.mutate(1.1)
        for allele in newchr:
            self.assertTrue(allele not in [z,z,'y',3,4])
        self.assertNotEqual(self.chromosome.id, newchr.id)


    def testNoMutate(self):
        newchr = self.chromosome.mutate(0)
        self.assertEqual(newchr.genes[0], self.gene)
        self.assertEqual(self.chromosome.id, newchr.id)


if __name__ == '__main__':
    unittest.main()
