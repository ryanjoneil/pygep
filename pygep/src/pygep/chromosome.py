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
Provides standard GEP chromosomes as well as the symbol decorator for
defining functions for use in chromosomes.  Note that the Chromosome 
class is an abstract base class, providing methods for construction and 
evaluation of genes.  Chromosomes that inherit from it should provide
a set of terminal and function symbols.
'''

from pygep.functions.linkers import default_linker
from pygep.gene import KarvaGene
from pygep.util import cache
import random


def symbol(symb):
    '''
    Decorator that assigns a symbol to a function for chromosome 
    display. The symbol is stored in the function.symbol attribute.

        @symbol('/')
        def divide(x, y):
            return x / y
    
    @param symb: symbol to use, typically one character
    '''
    def decorator(func):
        '''
        Attaches a symbol to a function as its 'symbol' attribute
        @param func: function to decorate
        '''
        func.symbol = symb
        return func

    return decorator


class MetaChromosome(type):
    '''
    Metaclass for computing various information about a chromosomal
    type.  Sets the following attributes on a chromosome class:
        - arity:   maximum functional arity
        - symbols: symbols that can reside in the head
    Also turns caching of fitness values on for all chromosomes.
    '''
    def __new__(mcs, name, bases, dct):
        '''
        Prepares a chromosome type for use in GEP, assigning to 
        cls.symbols, cls.arity, and caching the cls._fitness.
        
        @param mcs:   class to apply the metaclass to
        @param name:  name of the class
        @param bases: base classes
        @param dct:   class dict
        '''
        typ = type.__new__(mcs, name, bases, dct)
        typ.symbols = typ.functions + typ.terminals

        # Find the max arity
        try:
            typ.arity = max([f.func_code.co_argcount for f in typ.functions])
        except ValueError:
            typ.arity = 0

        # Cache fitness values
        typ._fitness = cache(typ._fitness)
        return typ


class Chromosome(object):
    '''
    A Chromosome must provide these attributes:
        - functions: tuple of nonterminals
        - terminals: tuple of terminal symbols

    And override these functions:
        - _fitness: fitness of a given individual
        - _solved:  True if the problem is optimally solved (optional)

    An example Chromosome that evolves simple arithmetic expressions
    on data objects providing attributes 'a' and 'b' and the constants
    1 and 2:

        from pygep.functions.arithmetic import *
        from pygep import Chromosome

        class Calculation(Chromosome):
            functions = multiply, add, subtract, divide
            terminals = 'a', 1, 2

            def _fitness(self):
                # Evaluate chromosome fitness here.
                # This often involves calling self.evaluate(something)

            def _solved(self):
                # Not required, but useful if the problem can
                # be optimally solved.  Usually this just means
                # checking self.fitness.
    '''
    __metaclass__ = MetaChromosome
    __next_id = 1
    gene_type = KarvaGene


    functions = ()
    terminals = ()
    symbols   = () # overridden by metaclass
    head = tail = length = arity = 0
    

    @classmethod
    def generate(cls, head, genes=1, linker=default_linker):
        '''
        Returns a generator of random GEP chromosomes
        @param head:   head length (min=0)
        @param genes:  number of genes (min=1)
        @param linker: linking function
        '''
        tail = head * (cls.arity - 1) + 1

        while True:
            new_genes = [None] * genes
            for i in xrange(genes):
                new_genes[i] = cls.gene_type(
                    [random.choice(cls.symbols)   for _ in xrange(head)] + \
                    [random.choice(cls.terminals) for _ in xrange(tail)], head
                )

            yield cls(new_genes, head, linker)


    def __init__(self, genes, head, linker=default_linker):
        '''
        Instantiates a chromsome instance and analyzes it for evaluation.
        Sets the self.coding tuple to the last genes in the coding regions
        and various other internal data for the chromosome.  Note that it
        is generally unwise to instantiate chromosomes manually.  It is
        much more common to create them via calls to the static method
        Chromosome.generate(...).

        @param genes:  genes in the chromosome
        @param head:   length (not index) of the gene heads (min=0)
        @param linker: linker function for gene evaluation
        '''
        # Must have at least one gene and a head length of 0
        if head < 0:
            raise ValueError('Head length must be at least 0')
        if not genes:
            raise ValueError('Must have at least 1 gene')

        self.genes  = genes
        self.head   = head
        self.linker = linker

        # Unique number of the organism
        self.__id = type(self).__next_id
        type(self).__next_id += 1

    
    def __cmp__(self, other):
        '''@return: cmp value of two chromosomes by fitness'''
        if self is other:
            return 0
        
        return cmp(self.fitness, other.fitness)


    def __len__(self):
        '''@return: total number of alleles in the chromosome'''
        return sum(len(g) for g in self.genes)


    def __iter__(self):
        '''@return: generator for alleles in chromosome'''
        for gene in self.genes:
            for allele in gene:
                yield allele    

    
    def __getitem__(self, i):
        '''
        Returns a given allele by index
        @param i: allele index
        @return:  allele
        '''
        i, j = divmod(i, len(self.genes))
        return self.genes[j][i]


    @cache
    def __repr__(self):
        '''@return: repr of chromosome alleles'''
        return ''.join(repr(g) for g in self.genes)


    def _child(self, genes):
        '''
        Creates a child chromosome
        @param genes: ordered list of GEP genes
        @return:      a child chromosome of self
        '''
        if genes != self.genes:
            return type(self)(genes, self.head, self.linker)
        return self


    # Unique ID of the organism
    id = property(lambda self: self.__id, doc='Organism #')


    def __call__(self, obj):
        '''
        Evaluates a given GEP chromosome against some instance.  The
        terminals in the chromosome are assumed to be attributes on
        the object instance provided (unless they are numeric constants).

        @param obj: an object instance with terminal attributes set
        @return:    result of evaluating the chromosome
        '''
        return self.linker(*[g(obj) for g in self.genes])


    def _fitness(self):
        '''@return: comparable fitness value'''
        raise NotImplementedError('Must override Chromosome._fitness')

    def _solved(self):
        '''@return: boolean indicating optimal solution found'''
        return False

    fitness = property(lambda self: self._fitness(), doc='Fitness value')
    solved  = property(lambda self: self._solved(),  doc='Problem solved')


    def mutate(self, rate):
        '''
        Produces a new chromosome via potential point mutation on each
        locus.  If nothing changes, the original chromosome is returned.

        @param rate: mutation rate per locus
        @return:     child chromosome (or self)
        '''
        genes = list(self.genes)
        
        # Traverse the chromosome gene by gene
        for gene_idx, gene in enumerate(self.genes):
            # Then locus by locus
            replacements = []
            for i, allele in enumerate(gene):
                # Do we mutate this locus?
                if random.random() < rate:
                    # Mutation within the tail can only use terminals
                    if i >= self.head:
                        new_allele = random.choice(self.terminals)
                    else:
                        new_allele = random.choice(self.symbols)
                    
                    # Only use this if the mutation actually did something
                    if new_allele != allele:
                        replacements.append((i, [new_allele]))


            # If we have actual replacements to make, do them
            if replacements:
                genes[gene_idx] = gene.derive(replacements)
            
        # Create a child of this chromosome
        return self._child(genes)


    def invert(self):
        '''
        Produces a new chromosome via head inversion
        @return: child chromosome
        '''
        if self.head < 2: # Head inversion does nothing in this case
            return self

        genes = list(self.genes)

        # Choose a random gene and two points within the head
        i = random.choice(xrange(len(self.genes)))
        start, stop = random.sample(xrange(self.head), 2)

        # Order the indexes correctly
        if start > stop:
            start, stop = stop, start

        # Create the new chromosome
        replacement = list(reversed(genes[i][start:stop+1]))
        genes[i] = genes[i].derive([(start, replacement)])
        return self._child(genes)


    def transpose_is(self, length):
        '''
        Produces a new chromosome via IS transposition
        @param length: sequence length (typically 1, 2, or 3)
        @return:       child chromosome
        '''
        # Since IS does not transpose to the root, it has no purpose
        # if the head length is less than 2.
        if self.head < 2:
            return self

        # Pick source and target genes
        genes  = list(self.genes)
        source = random.choice(genes)
        target = random.choice(xrange(len(genes)))

        # Extract a transposition sequence. Truncate if required.
        start = random.choice(xrange(len(source)))
        end   = start + length
        end   = self.head if end > self.head else end

        # Offset into target gene: in the head but not the root
        offset = random.choice(xrange(1, self.head))

        # Insert into the target gene's head
        replacement = source[start:end][:self.head-offset] + \
                      genes[target][offset:self.head-end+start]
        genes[target] = genes[target].derive([(offset, replacement)])
        return self._child(genes)


    def transpose_ris(self, length):
        '''
        Produces a new chromosome via RIS transposition
        @param length: sequence length (typically 1, 2, or 3)
        @return:       child chromosome
        '''
        # Pick source and target genes
        genes  = list(self.genes)
        source = random.choice(genes)
        target = random.choice(xrange(len(genes)))

        # Extract a transposition sequence. Truncate if required.
        # For RIS the sequence must begin with a function.
        try:
            start = random.choice(
                [i for i in xrange(len(source)) if callable(source[i])]
            )
        except IndexError: # no functions!
            return self

        end = start + length
        end = self.head if end > self.head else end

        # Insert into the target gene's head at position 0
        replacement   = source[start:end] + genes[target][:self.head+start-end]
        genes[target] = genes[target].derive([(0, replacement)])
        return self._child(genes)


    def transpose_gene(self):
        '''
        Produces a new chromosome via gene transposition
        @return: child chromosome
        '''
        if len(self.genes) < 2:
            return self
        
        genes = list(self.genes)
        which = random.randint(1, len(genes)-1)
        
        # Switch these genes
        genes[0], genes[which] = genes[which], genes[0]
        return self._child(genes)


    def crossover_one_point(self, other):
        '''
        Produces two children via one-point crossover
        @param other: second parent
        @return:      child 1, child 2
        '''
        genes1, genes2 = list(self.genes), list(other.genes)
        
        # Pick a gene and index to crossover at
        gene  = random.choice(xrange(len(genes1)))
        index = random.choice(xrange(len(genes1[gene])))
        
        # Construct new child genes
        child1 = genes1[gene].derive([(index, genes2[gene][index:])])
        child2 = genes2[gene].derive([(index, genes1[gene][index:])])
        genes1[gene], genes2[gene] = child1, child2
        return self._child(genes1), other._child(genes2)


    def crossover_two_point(self, other):
        '''
        Produces two children via two-point crossover
        @param other: second parent
        @return:      child 1, child 2
        '''
        if len(self) < 2:
            return self, other

        genes1, genes2 = list(self.genes), list(other.genes)

        # Choose start and stop loci
        ind1, ind2 = random.sample(xrange(len(self)), 2)
        if ind1 > ind2:
            ind1, ind2 = ind2, ind1
        
        # Convert these to gene and allele numbers
        gene_length = len(self.genes[0])
        ind1, allele1 = divmod(ind1, gene_length)
        ind2, allele2 = divmod(ind2, gene_length)

        # Switch genes in between the modified genes
        if ind2 - ind1 > 1:
            start = ind1 + 1
            genes1[start:ind2], genes2[start:ind2] = \
                genes2[start:ind2], genes1[start:ind2]
        
        # And switch components of the start and stop genes
        child1 = genes1[ind1].derive([(allele1, genes2[ind1][allele1:])])
        child2 = genes2[ind1].derive([(allele1, genes1[ind1][allele1:])])
        genes1[ind1], genes2[ind1] = child1, child2
            
        child1 = genes1[ind2].derive([(0, genes2[ind2][:allele2])])
        child2 = genes2[ind2].derive([(0, genes1[ind2][:allele2])])
        genes1[ind2], genes2[ind2] = child1, child2
        
        return self._child(genes1), other._child(genes2)


    def crossover_gene(self, other):
        '''
        Produces two children via full gene crossover
        @param other: second parent
        @return:      child 1, child 2
        '''
        genes1, genes2 = list(self.genes), list(other.genes)

        # Choose a random gene
        gene = random.choice(xrange(len(genes1)))
        genes1[gene], genes2[gene] = genes2[gene], genes1[gene]
        return self._child(genes1), other._child(genes2)
