#!/usr/bin/env python2.5
from pygep import *
from pygep.functions.arithmetic import *
from pygep.functions.comparison import *
from pygep.functions.linkers import sum_linker
import string, sys


# This test is based on one from C. Ferreira's book.
# The cancer1.dt data set is available for download
# from ftp.ira.uka.de//pub/neuron/proben1.tar.gz


# This class represents information about a tumor
# with a specified number of variables
VARS = tuple([l for l in string.lowercase[:9]])
class Tumor(object):
    def __init__(self, line):
        row = line.strip().split()
        for letter, val in zip(VARS, row):
            setattr(self, letter, float(val))

        # The tumor can either be benign or malignant
        if row[-2:] == ['1','0']:
            self.benign = True
        elif row[-2:] == ['0','1']:
            self.benign = False
        else:
            raise ValueError('Invalid data row %r' % line)


# We need two samples: one for training our GEP
# chromosomes on and another for final evaluation
TRAIN_SIZE, TRAIN_SAMPLE = 350, []
TEST_SIZE, TEST_SAMPLE = 174, []


# We also need to know how many tumors are benign
# or malignant for the training data.
TRAIN_BENIGN = TRAIN_MALIG = 0


# Our chromosomes attempt to determine which tumors are
# benign and which are not
class TumorEvaluator(Chromosome):
    functions = (multiply, add, subtract, divide, power, root, \
                 equal, unequal, less, greater, less_or_equal, \
                 greater_or_equal) * 5
    terminals = VARS

    def _fitness(self):
        try:
            correct = 0
            for tumor in TRAIN_SAMPLE:
                # Make a prediction about the tumor
                benign = self(tumor) > 0

                # And see if it's right...
                if benign == tumor.benign:
                    correct += 1

            # Fitness if the number of hits assuming we at least
            # pass the threshold of a minimum # correct.
            if correct >= max(TRAIN_BENIGN, TRAIN_MALIG):
                return correct
            else:
                return 0

        except:
            return 0 # nonviable

    def _solved(self):
        self.fitness == len(TRAIN_SAMPLE)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: %s cancer1.dt' % sys.argv[0]
        sys.exit()

    # Read in the training and testing data
    data = open(sys.argv[1]).readlines()[7:] # skip header
    TRAIN_SAMPLE.extend([Tumor(line) for line in data[:TRAIN_SIZE]])
    TEST_SAMPLE.extend([Tumor(line) for line in data[-TEST_SIZE:]])

    # Determine training stats
    for tumor in TRAIN_SAMPLE:
        if tumor.benign:
            TRAIN_BENIGN += 1
        else:
            TRAIN_MALIG += 1

    # Create our population and find a solution
    p = Population(TumorEvaluator, 50, 8, 4, sum_linker)
    print p
    p.is_transposition_rate = 1

    for _ in xrange(50):
        if p.best.solved:
            break
        p.cycle()
        print
        print p

    print
    if p.best.solved:
        print 'SOLVED:', p.best
    else:
        print 'UNSOLVED:', p.best

    # See how the best trained individual does on the test sample
    l, correct = len(TEST_SAMPLE), 0
    for tumor in TEST_SAMPLE:
        try:
            benign = p.best(tumor) > 0
            if benign == tumor.benign:
                correct += 1
        except:
            pass

    print 'SCORE: %d / %d = %0.3f' % (correct, l, correct / float(l)),
