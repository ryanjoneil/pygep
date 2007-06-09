# PyGEP: Gene Expression Programming for Python
# Copyright (C) 2007  Ryan J. O'Neil
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

'''
Provides a Population class for managing multiple GEP chromosomes
over time, allowing selection, replication, and variation operators.
'''

from itertools import izip
from pygep.functions.linkers import default_linker
from pygep.util import stats
import random, string


class Population(object):
    '''
    A Population instance has the following default configuration:
        - exclusion_level:          selection pressure (typically 1.5)
        - mutation_rate:            mutation rate (2 per chromosome)
        - inversion_rate:           inversion probability (0.1)
        - is_transposition_rate:    non-root transposition (0.1)
        - is_transposition_length:  IS transposition lengths (1,2,3)
        - ris_transposition_rate:   root transposition rate (0.1)
        - ris_transposition_length: RIS transposition lengths (1,2,3)
        - gene_transposition_rate:  gene transposition rate (0.1)
        - crossover_one_point_rate: 1-point crossover rate (0.3)
        - crossover_two_point_rate: 2-point crossover rate (0.3)
        - crossover_gene_rate:      full gene crossover (0.1)

    Mutation, by default, is set to a rate where it will modify
    about two loci per chromosome.  Example Population usage::

        from pygep.functions.linkers import *
        from pygep import *

        p = Population(Chromosome, population-size, head-length, 
                       number-genes, ET-linker-function)
              
        for _ in xrange(50): # maximum number of generations
            if p.best.solved:
                break
            p.cycle() # recombine and select next generation
    '''
    exclusion_level          = 1.5
    mutation_rate            = 0.0 # Set by __init__
    inversion_rate           = 0.1
    is_transposition_rate    = 0.1
    is_transposition_length  = 1, 2, 3
    ris_transposition_rate   = 0.1
    ris_transposition_length = 1, 2, 3
    gene_transposition_rate  = 0.1
    crossover_one_point_rate = 0.3
    crossover_two_point_rate = 0.3
    crossover_gene_rate      = 0.1


    def __init__(self, cls, size, head, genes=1, linker=default_linker):
        '''
        Generates a population of some chromsome class
        @param cls:    Chromosome type
        @param size:   population size
        @param head:   chromosome head length (min=0)
        @param genes:  number of genes (min=1)
        @param linker: multigenic results linker function
        '''
        self.size   = size
        self.head   = head
        self.genes  = genes
        self.linker = linker

        self.__age = 0

        # Start an initial population
        self.population = [i for _, i in izip(xrange(size),
                           cls.generate(head, genes, linker))]
        self._next_pop = [None] * size # placeholder for next generation
        self._scaled   = [None] * size # fitness scaling

        # Header for display purposes
        try:
            chr_length = len(self.population[0])
            self.header = string.digits * (chr_length / len(string.digits)) + \
                          string.digits[:(chr_length % len(string.digits))]
            self.header += '\n' + '-' * len(self.header)
        except IndexError:
            raise ValueError('Empty populations are meaningless!')

        # Determine mutation rate
        self.mutation_rate = 2.0 / chr_length
        
        # Compute stats about the initial generation
        self.stdev = self.mean = 0
        self._update_stats()


    def __repr__(self):
        '''@return: repr of population with header and statistical info'''
        header = '[Generation: %s  |  Best: #%s (%s)  |  Mean: %0.1f]\n%s' % \
            (self.age, self.best.id, self.best.fitness, self.mean, self.header)
        max_id_len = max(len(str(i.id)) for i in self)
        return '\n'.join([header] + [
            '%s [%s]: %s' % (i, str(i.id).rjust(max_id_len), i.fitness)
            for i in self
        ])


    def __len__(self):
        '''@return: number of chromosomes in the population'''
        return self.size


    def __iter__(self):
        '''@return: iterator over population chromosomes'''
        return iter(self.population)

    
    def __getitem__(self, i):
        '''@return: a given chromosome number'''
        return self.population[i]


    def _update_stats(self):
        '''Assigns to self.mean and stdev population fitness stats'''
        self.mean, self.stdev, _ = stats.fitness_stats(self)


    age  = property(lambda self: self.__age, doc='Generation number')
    best = property(
        # Gives preference to later individuals tied for best
        lambda self: max(reversed(self.population)),
        doc='The best Chromosome of the current generation'
    )


    def solve(self, generations):
        '''
        Cycles a number of generations. Stops if self.solved()
        @param generations: # of genrations to give up after
        '''
        for _ in xrange(generations):
            if self.best.solved:
                break
            self.cycle()


    def cycle(self):
        '''Selects, replicates and recombines the next generation'''
        # Copy the best individual via simple elitism
        self._next_pop[0] = self.best

        if self.mean > 0:
            # Fill in the rest through fitness scaling. First compute the
            # sigma-scaled fitness proportionate value for each chromosome.
            for i, j in enumerate(self.population):
                self._scaled[i] = self.exclusion_level * j.fitness / self.mean
            scaling = sum(self._scaled)

            # Then generate n-1 spins of the roulette wheel
            select = [random.random() * scaling for _ in xrange(self.size-1)]
            select.sort()

            # Move through the current population, calculating a window
            # for each scaled fitness.  However many of the sorted roulette
            # spins are within that window yields the number of copies.
            window = self._scaled[0]
            source, target = 0, 1
            for scaled in select:
                # Move to the element that covers our range
                while window < scaled:
                    source += 1
                    try:
                        window += self._scaled[source]
                    except IndexError: # possible floating-point errors
                        source = self.size - 1
                        break

                # Copy this element to the next generation
                self._next_pop[target] = self.population[source]
                target += 1

        else:
            # Mean fitness <= 0.  Since no chromosome should ever have a
            # negative fitness, this should mean all organisms are inviable.
            # In this case we shall content ourselves to choose randomy.
            for i in xrange(self.size):
                self._next_pop[i] = random.choice(self.population)


        # Recombination section - always exclude best
        #
        # Mutation occurs potentially for each allele in each chromosome
        # Inversion & transposition are considered for each chromosome
        for i in xrange(1, self.size):
            # Try and mutate each individual
            if self.mutation_rate:
                self._next_pop[i] = self._next_pop[i].mutate(self.mutation_rate)
                
            # Then inversion
            if self.inversion_rate and random.random() < self.inversion_rate:
                self._next_pop[i] = self._next_pop[i].invert()

            # Insertion Sequence transposition
            if self.is_transposition_rate and \
               random.random() < self.is_transposition_rate:
                self._next_pop[i] = self._next_pop[i].transpose_is(
                    random.choice(self.is_transposition_length))

            # Root Insert Sequence transposition
            if self.ris_transposition_rate and \
               random.random() < self.ris_transposition_rate:
                self._next_pop[i] = self._next_pop[i].transpose_ris(
                    random.choice(self.ris_transposition_length))

            # Gene transposition
            if self.gene_transposition_rate and \
               random.random() < self.gene_transposition_rate:
                self._next_pop[i] = self._next_pop[i].transpose_gene()

        # Then try one|two-point and gene crossover - exclude best
        for i, j in self._pairs(self.crossover_one_point_rate):
            par1, par2 = self._next_pop[i], self._next_pop[j]            
            children   = par1.crossover_one_point(par2)
            self._next_pop[i], self._next_pop[j] = children

        for i, j in self._pairs(self.crossover_two_point_rate):
            par1, par2 = self._next_pop[i], self._next_pop[j]
            children   = par1.crossover_two_point(par2)
            self._next_pop[i], self._next_pop[j] = children

        for i, j in self._pairs(self.crossover_gene_rate):
            par1, par2 = self._next_pop[i], self._next_pop[j]
            children   = par1.crossover_gene(par2)
            self._next_pop[i], self._next_pop[j] = children

        # Switch to the next generation and increment age
        self._next_pop, self.population = self.population, self._next_pop
        self.__age += 1
        self._update_stats()


    def _pairs(self, rate):
        '''
        Generats of random index pairs for crossover
        @param rate: crossover rate
        @return:     ((p1a-index, p1b-index), (p2a-index, p2b-index), ...)
        '''
        # Crossover requires at least 3 individuals since the first isn't used
        if rate and self.size >= 3:
            # Choose and shuffle the individuals to participate in crossover
            orgs = [i for i in xrange(1, self.size) if random.random() < rate]
            random.shuffle(orgs)
            
            # Generate pairs of indexes.  If there is an odd man out, ignore him.
            for i in xrange(0, len(orgs), 2):
                try:
                    yield orgs[i], orgs[i+1]
                except IndexError:
                    pass
