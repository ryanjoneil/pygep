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


class ZeroFitnessComputation(SillyComputation):
    def _fitness(self):
        return 0
    
    def _solved(self):
        return True


class PopulationTest(unittest.TestCase):
    '''Tests population cycling'''
    def setUp(self):
        self.pop = Population(SillyComputation, 10, 5, 1)
        
        # Turn all variation on all the time
        self.pop.mutation_rate            = 1.1 # additional .1 = sanity check
        self.pop.inversion_rate           = 1.1
        self.pop.is_transposition_rate    = 1.1
        self.pop.ris_transposition_rate   = 1.1
        self.pop.gene_transposition_rate  = 1.1
        self.pop.crossover_one_point_rate = 1.1
        self.pop.crossover_two_point_rate = 1.1
        self.pop.crossover_gene_rate      = 1.1
    
    
    def testBestFitness(self):
        for c in self.pop:
            self.assertTrue(self.pop.best >= c)
    
    
    def testCycle(self):
        self.assertEqual(self.pop.age, 0)
        first_best = self.pop.best
        
        self.pop.solve(1)
        self.assertEqual(self.pop.age, 1)
        self.assertEqual(len(self.pop), 10)
        self.assertTrue(self.pop[0] is first_best)
        
        
    def testZeroFitness(self):
        # Special case: mean fitness <= 0
        p = Population(ZeroFitnessComputation, 10, 5, 1)
        p.cycle()
        self.assertEqual(0, p.mean)
        self.assertEqual(0, p.stdev)
        

    def testStopOnSolve(self):
        p = Population(ZeroFitnessComputation, 10, 5, 1)
        p.solve(100)
        self.assertEqual(0, p.age)
    
    
    def testEmptyPopulation(self):
        self.assertRaises(ValueError, Population, SillyComputation, 0, 5, 1)
    
    
    def testPopulationRepr(self):
        p = repr(self.pop)
        for c in self.pop:
            self.assertTrue(repr(c) in p)


if __name__ == '__main__':
    unittest.main()
