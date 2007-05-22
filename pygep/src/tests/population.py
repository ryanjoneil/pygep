from pygep import Population
from pygep.gene import KarvaGene
from tests.base import Computation
import unittest


class SillyData(object):
    a = 5


class SillyComputation(Computation):
    silly = SillyData()
    def _fitness(self):
        try:
            return max(self(self.silly), 0)
        except ZeroDivisionError:
            return 0


class PopulationTest(unittest.TestCase):
    '''Tests population cycling'''
    def setUp(self):
        self.pop = Population(SillyComputation, 10, 5, 1)
    
    
    def testBestFitness(self):
        for c in self.pop:
            self.assertTrue(self.pop.best >= c)
    
    
    def testCycle(self):
        self.assertEqual(self.pop.age, 0)
        self.pop.cycle()
        self.assertEqual(self.pop.age, 1)
        self.assertEqual(len(self.pop), 10)
    

if __name__ == '__main__':
    unittest.main()
