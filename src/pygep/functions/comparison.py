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
Provides basic comparison non-terminals.  If each is true, it returns
the first value given.  If false, it returns the second.

Common comparison non-terminal functions:
    - (=) equal
    - (U) unequal
    - (<) less
    - (>) greater
    - (L) less_or_equal
    - (G) greater_or_equal
'''

from pygep.chromosome import symbol


__all__ = 'equal', 'unequal', 'less', 'greater', 'less_or_equal', \
          'greater_or_equal'


@symbol('=')
def equal(i, j):
    '''@return: i if i == j else j'''
    return i if i == j else j


@symbol('U')
def unequal(i, j):
    '''@return: i if i != j else j'''
    return i if i != j else j


@symbol('<')
def less(i, j):
    '''@return: i if i < j else j'''
    return i if i < j else j


@symbol('>')
def greater(i, j):
    '''@return: i if i > j else j'''
    return i if i > j else j


@symbol('L')
def less_or_equal(i, j):
    '''@return: i if i <= j else j'''
    return i if i <= j else j


@symbol('G')
def greater_or_equal(i, j):
    '''@return: i if i >= j else j'''
    return i if i >= j else j
