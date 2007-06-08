from pygep.functions.math.arithmetic import add_op, subtract_op
from pygep.gene import KarvaGene
import unittest


class Foo(object):
    a = 5.


class KarvaTest(unittest.TestCase):
    '''Tests basic functionality of Karva genes'''
    def setUp(self):
        self.gene = KarvaGene([add_op, subtract_op, 'a', 1, 'a'], 2)
    
    
    def testEvaluation(self):
        f = Foo()
        self.assertEqual(1, self.gene(f))
        self.assertTrue(f in getattr(self.gene, self.gene.__call__.memo))
        

    def testCodingLocation(self):
        self.assertEqual(4, self.gene.coding)
        self.assertEqual(0, self.gene.derive([(0, ['a'])]).coding)
    
    
    def testDerivation(self):
        g = self.gene.derive([(0, ['a']), (3, [add_op, add_op])])
        self.assertEqual(['a', subtract_op, 'a', add_op, add_op], g.alleles)
        self.assertEqual(self.gene, self.gene.derive([(2, ['a'])]))
    
    
    def testRepresentation(self):
        self.assertEqual('+-a1a', repr(self.gene))
        
    
    def testTerminalLocations(self):
        self.assertEqual(self.gene._terminals, [('a', [2,4])])


if __name__ == '__main__':
    unittest.main()
