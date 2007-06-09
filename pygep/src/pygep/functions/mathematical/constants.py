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
Common constant functions:
    - (0) zero_op: 0
    - (1) one_op:  1
    - (P) pi_op:   math.pi
    - (E) e_op:    math.e
'''

from pygep.chromosome import symbol
import math


__all__ = 'CONSTANTS_ALL', 'CONSTANTS_ARITY_0'


zero_op = symbol('0')(lambda: 0)
one_op  = symbol('1')(lambda: 1)
pi_op   = symbol('P')(lambda: math.pi)
e_op    = symbol('E')(lambda: math.e)


CONSTANTS_ARITY_0 = zero_op, one_op, pi_op, e_op
CONSTANTS_ALL = CONSTANTS_ARITY_0
