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
    - (=) equal_op:            i if i == j else j
    - (U) unequal_op:          i if i != j else j
    - (<) less_op:             i if i < j else j
    - (>) greater_op:          i if i > j else j
    - (L) less_or_equal_op:    i if i <= j else j
    - (G) greater_or_equal_op: i if i >= j else j
'''

from pygep.chromosome import symbol


__all__ = 'COMPARISON_ALL', 'COMPARISON_ARITY_2'


equal_op            = symbol('=')(lambda i, j: i if i == j else j)
unequal_op          = symbol('U')(lambda i, j: i if i != j else j)
less_op             = symbol('<')(lambda i, j: i if i < j  else j)
greater_op          = symbol('>')(lambda i, j: i if i > j  else j)
less_or_equal_op    = symbol('L')(lambda i, j: i if i <= j else j)
greater_or_equal_op = symbol('G')(lambda i, j: i if i >= j else j)


COMPARISON_ARITY_2 = equal_op, unequal_op, less_op, greater_op, \
                     less_or_equal_op, greater_or_equal_op
COMPARISON_ALL = COMPARISON_ARITY_2
