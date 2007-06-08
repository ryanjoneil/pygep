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
Common hyperbolic functions:
    - (SINH) sineh_op:      math.sinh(x)
    - (COSH) cosineh_op:    math.cosh(x)
    - (TANH) tangenth_op:   math.tanh(x)
    - (CSCH) cosecanth_op:  1 / math.sinh(x)
    - (SECH) secanth_op:    1 / math.cosh(x)
    - (COTH) cotangenth_op: 1 / math.tanh(x)
'''

from pygep.chromosome import symbol
import math


__all__ = 'HYPERBOLIC_ALL', 'HYPERBOLIC_ARITY_1'


sineh_op      = symbol('SINH')(lambda i: math.sinh(i))
cosineh_op    = symbol('COSH')(lambda i: math.cosh(i))
tangenth_op   = symbol('TANH')(lambda i: math.tanh(i))
cosecanth_op  = symbol('CSCH')(lambda i: 1. / math.sinh(i))
secanth_op    = symbol('SECH')(lambda i: 1. / math.cosh(i))
cotangenth_op = symbol('COTH')(lambda i: 1. / math.tanh(i))


HYPERBOLIC_ARITY_1 = sineh_op, cosineh_op, tangenth_op, cosecanth_op, \
                     secanth_op, cotangenth_op
HYPERBOLIC_ALL = HYPERBOLIC_ARITY_1
