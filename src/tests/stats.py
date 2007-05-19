from pygep.util.stats import fitness_stats
import math, unittest


class Fitness(object):
    '''Duck-typed class for fitness testing'''
    def __init__(self, fitness):
        self.fitness = fitness


class FitnessStatsTest(unittest.TestCase):
    '''Tests basic statistical computations of fitness'''
    def testStats(self):
        population = [Fitness(float(x)) for x in range(1,4)]
        mean, stdev, total = fitness_stats(population)

        self.assertEqual(2.0, mean)
        self.assertEqual(math.sqrt(2./3), stdev)
        self.assertEqual(6.0, total)


if __name__ == '__main__':
    unittest.main()

