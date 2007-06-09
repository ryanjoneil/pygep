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
Common exponential and logarithmic non-terminal functions and symbols:
    - (LN   ) ln_op:        math.log(x)
    - (LOG10) log10_op:     math.log10(x)
    - (^    ) power_op:     x ** y
    - (E^   ) exp_op:       e ** x
    - (10^  ) pow10_op:     10 ** x
    - (^2   ) square_op:    x ** 2
    - (^3   ) cube_op:      x ** 3
    - (Q    ) root_op:      math.sqrt(x)
    - (Q3   ) cube_root_op: x ** (1./3)
    - (^-1  ) inverse_op:   1 / x
'''

from pygep.chromosome import symbol
import math


__all__ = 'POWER_ALL', 'POWER_ARITY_1', 'POWER_ARITY_2'


ln_op        = symbol('LN'   )(lambda i: math.log(i))
log10_op     = symbol('LOG10')(lambda i: math.log10(i))
power_op     = symbol('^'    )(lambda i, j: i ** j)
exp_op       = symbol('E^'   )(lambda i: math.exp(i))
pow10_op     = symbol('10^'  )(lambda i: 10 ** i)
square_op    = symbol('^2'   )(lambda i: i ** 2)
cube_op      = symbol('^3'   )(lambda i: i ** 3)
root_op      = symbol('Q'    )(lambda i: math.sqrt(i))
cube_root_op = symbol('Q3'   )(lambda i: i ** (1./3))
inverse_op   = symbol('^-1'  )(lambda i: 1. / i)


POWER_ARITY_1 = ln_op, log10_op, root_op, exp_op, pow10_op, square_op, \
                cube_op, inverse_op
POWER_ARITY_2 = power_op,
POWER_ALL = POWER_ARITY_1 + POWER_ARITY_2
