from pygep.chromosome import Chromosome, symbol
from pygep.functions.mathematical.arithmetic import ARITHMETIC_ALL


'''Base types for use in other tests'''


class Computation(Chromosome):
    ARITY = 2
    functions = ARITHMETIC_ALL
    terminals = 'a', 1, 2
