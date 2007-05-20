from pygep.chromosome import Chromosome, symbol
from pygep.functions.arithmetic import *


'''Base types for use in other tests'''


class Computation(Chromosome):
    ARITY = 2
    functions = multiply, add, subtract, divide
    terminals = 'a', 1, 2
