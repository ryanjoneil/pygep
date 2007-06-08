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
Provides basic logical operators: and, or, not, if.  These are same to use
with the mathematics operators as they return either 1, 0 or the types 
passed in to them.

Common logic non-terminal functions:
    - (&) and_op: i if i and j else 0
    - (|) or_op:  i or j or 0
    - (!) not_op: 0 if i else 1
    - (I) if_op:  j if i else k
'''

from pygep.chromosome import symbol


__all__ = 'LOGIC_ALL', 'LOGIC_ARITY_1', 'LOGIC_ARITY_2', 'LOGIC_ARITY_3'


and_op = symbol('&')(lambda i, j: i if i and j else 0)
or_op  = symbol('|')(lambda i, j: i or j or 0)
not_op = symbol('!')(lambda i: 0 if i else 1)
if_op  = symbol('I')(lambda i, j, k: j if i else k)


LOGIC_ARITY_1 = not_op,
LOGIC_ARITY_2 = and_op, or_op
LOGIC_ARITY_3 = if_op,
LOGIC_ALL = LOGIC_ARITY_1 + LOGIC_ARITY_2 + LOGIC_ARITY_3
