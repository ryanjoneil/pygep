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
Provides Karva genes, the unigenic building block used in GEP
for multigenic chromosomes.  This allows one to cache chromosome
evaluation more efficiently.
'''

from copy import copy
from itertools import groupby
from operator import itemgetter
from pygep.util import memoize


class KarvaGene(object):
    '''
    Represents a single gene that is evaluated as Karva language.  
    These are intended only for internal use by the Chromosome class,
    which will generate the gene contents and link together one or 
    more genes.  Genes, in turn, are responsible for generating and
    caching evaluation results.
    '''
    def __init__(self, alleles, head):
        '''
        Instantiates a Karva style unigenic GEP chromosome
        @param alleles: list of individual loci for a given chromosome
        @param head:    head length
        '''
        self.alleles = alleles
        self.head    = head
        self.coding  = 0
        
        self._evaluation = self._terminals = []
        self._find_coding()

    
    @memoize
    def __call__(self, obj):
        '''
        Evaluates a Karva gene against some instance.  The string terminals in 
        the gene are assumed to be attributes on the object instance.  Numeric
        constants are left as is, and functions are evaluated.

        @param obj: some object instance
        @return:    result of evaluating the gene
        '''
        self._prepare_eval_attrs(obj)
        
        # Evaluate the gene against obj in reverse
        index = self.coding + 1
        for i in reversed(xrange(index)):
            allele = self.alleles[i]

            if callable(allele):
                num  = allele.func_code.co_argcount
                args = self._evaluation[index-num:index]

                # Replace the operation in eval with its return val
                self._evaluation[i] = allele(*args)
                index -= num

        # Expression results will always be stored in the first index
        return self._evaluation[0]


    def __repr__(self):
        '''@return: repr of gene alleles'''
        gene_str = ''
        for allele in self.alleles:
            # Differentiate between functions and terminals
            try:
                name = allele.symbol
            except AttributeError:
                try:
                    name = allele.__name__
                except AttributeError:
                    name = str(allele)

            # If the name is not one char, surround it with { }
            gene_str += name if len(name) == 1 else '{%s}' % name

        return gene_str

    
    def __len__(self):
        '''@return: number of alleles in the gene'''
        return len(self.alleles)
    
    
    def __iter__(self):
        '''@return: iterator over gene alleles'''
        return iter(self.alleles)
    
    
    def __getitem__(self, i):
        '''@return: an individual allele from the gene'''
        return self.alleles[i]
    
    
    def __getslice__(self, i, j):
        '''@return: a slice of alleles'''
        return self.alleles[i:j]
    
    
    def _find_coding(self):
        '''
        Assigns the last coding index to self.coding and creates an 
        evaluation list from the coding region as self._evaluation
        and pairs of foreign attributes with locations at self._terminals.
        '''
        # How to find the length of a single coding region:
        #
        # Start at the first gene and determine how many args it
        # requires. Then move forward that many args and sum their
        # required args. Continue this until there are no more
        # required args. The resulting index will be one gene past
        # the coding region for the current gene
        index, args = 0, 1
        while args:
            next_args = 0
            for _ in xrange(args):
                if callable(self.alleles[index]):
                    next_args += self.alleles[index].func_code.co_argcount
                index += 1

            args = next_args

        self.coding = index - 1
        
        
        # The evaluation list only uses the coding region.  Since constants
        # done change from one run to the next, only expression results and
        # attribute values do, this is perfectly safe.
        self._evaluation = self.alleles[:self.coding+1]
        
        # TODO: consider converting NCs to floats in some future release
        #for i, allele in enumerate(self._evaluation): # ints -> floats
        #    if isinstance(allele, int):
        #        self._evaluation[i] = float(allele)
        
        # Pull out the attribute terminals by terminal name.  This constructs
        # a list of pairs containing attribute name and indexes:
        #
        #     [('a', [3,5]), ('b', [4]), ...]
        first = itemgetter(1)
        
        # Generates pairs of (index, terminal) for attribute terminals
        terminals = (i for i in enumerate(self._evaluation) 
                     if isinstance(i[1], str))
        
        # Groups those termianls into (terminal, [indexes])
        self._terminals = [
            (key, [i[0] for i in value]) for key, value in groupby(
                sorted(terminals, key=first), key=first
            )
        ]
    
    
    def _prepare_eval_attrs(self, obj):
        '''Pulls attributes from obj into the evaluation list'''
        # Prepare our evaluation list -> results of expression evalation
        for terminal, indexes in self._terminals:
            temp = getattr(obj, terminal)
            for i in indexes:
                self._evaluation[i] = temp
    
        
    def derive(self, changes):
        '''
        Derives a gene from self.  If the coding region remains unchanged,
        then the new gene keep the memoized evaluations of its parent. For 
        instance, replacing allele 0 with 'x' and allele 3 with a function
        add via point mutation would look like:
                        
            gene.derive([(0, ['x']), (3, [add]))
        
        Whereas replacing a block of alleles in crossover would like like:
        
            gene.derive([(5, [add, 'x', 'y'])])

        @param changes: sequence of (index, alleles) tuples
        @return: new KarvaGene
        '''
        new  = None # new gene
        same = True # whether or not the coding region is the same
        for index, alleles in changes:
            length = len(alleles)
            
            if self[index:index+length] != alleles:
                # Copy the alleles on first change
                if not new:
                    new = self[:index] + alleles + self[index+length:]
                else:
                    new[index:index+length] = alleles
                
                # Does this change the coding region?
                if same and index <= self.coding:
                    same = False
            
        if not new: # Nothing changed!
            return self
        
        # Create the new gene
        gene = copy(self)
        gene.alleles = new
        
        if not same: # Recalculate coding region & kill memoized results
            gene._find_coding()
            try:
                delattr(gene, self.__call__.memo)
            except AttributeError:
                pass
            
        return gene
