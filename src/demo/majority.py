from pygep import *
from pygep.functions.linkers import or_linker
from pygep.functions.logical import LOGIC_ALL

# Demo for the boolean majority function

class Majority(object):
    SAMPLE = []
    
    @staticmethod
    def populate():
        for a in 0, 1:
            for b in 0, 1:
                for c in 0, 1:
                    Majority.SAMPLE.append(Majority(a, b, c))
        
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.majority = (a and b) or (a and c) or (b and c)


class BooleanFunction(Chromosome):
    functions = LOGIC_ALL
    terminals = 'a', 'b', 'c'
    
    def _fitness(self):
        # Fitness function: number of hits
        hits = 0
        for i in Majority.SAMPLE:
            if i.majority == bool(self(i)):
                hits += 1
        
        return hits
    
    def _solved(self):
        return self.fitness >= len(Majority.SAMPLE)


if __name__ == '__main__':
    Majority.populate()

    # Search for a solution
    p = Population(BooleanFunction, 10, 3, 3, or_linker)
    print p

    for _ in xrange(100):
        if p.best.solved:
            break
        p.cycle()
        print
        print p
        
    if p.best.solved:
        print
        print 'SOLVED:', p.best
    