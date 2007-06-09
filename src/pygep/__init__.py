# PyGEP: Gene Expression Programming for Python
# Copyright (C) 2007  Ryan J. O'Neil
# http://code.google.com/p/pygep/
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
PyGEP: Gene Expression Programming for Python
Copyright (C) 2007  Ryan J. O'Neil
http://code.google.com/p/pygep/

PyGEP is a simple library suitable for academic study of GEP (Gene 
Expression Programming) in Python 2.5, aiming for ease of use and 
rapid implementation. It provides standard multigenic chromosomes; a 
population class using elitism and fitness scaling for selection;
mutation, crossover and transposition operators; and some standard 
GEP functions and linkers.

This software is released under the GPL 2.0.
'''

from pygep.chromosome import Chromosome
from pygep.population import Population

__version__ = '0.3.0'
__all__ = 'Chromosome', 'Population'
