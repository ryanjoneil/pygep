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
Common arithmetical non-terminal functions and symbols:
    - (*) multiply_op: x * y
    - (+) add_op:      x + y
    - (-) subtract_op: x - y
    - (/) divide_op:   x / y
    - (%) modulus_op:  x % y
'''

from pygep.chromosome import symbol


__all__ = 'ARITHMETIC_ALL', 'ARITHMETIC_ARITY_2'


# Functions of Arity 2
add_op      = symbol('+')(lambda i, j: i + j)
subtract_op = symbol('-')(lambda i, j: i - j)
multiply_op = symbol('*')(lambda i, j: i * j)
divide_op   = symbol('/')(lambda i, j: float(i) / j)
modulus_op  = symbol('%')(lambda i, j: i % j)


ARITHMETIC_ARITY_2 = add_op, subtract_op, multiply_op, divide_op, modulus_op
ARITHMETIC_ALL = ARITHMETIC_ARITY_2
