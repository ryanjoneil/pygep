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
    - (ln   ) ln_op:        math.log(x)
    - (log10) log10_op:     math.log10(x)
    - (^    ) power_op:     x ** y
    - (e^   ) exp_op:       e ** x
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


@symbol('ln')
def ln_op(i):
    '''
    @return: ln(i)
    @raise OverflowError: i == 0
    @raise ValueError: i < 0
    '''
    return math.log(i)


@symbol('log10')
def log10_op(i):
    '''
    @return: log10(i)
    @raise OverflowError: i == 0
    @raise ValueError: i < 0
    '''
    return math.log10(i)


@symbol('^')
def power_op(i, j):
    '''@return: i ** j'''
    return i ** j


@symbol('e^')
def exp_op(i):
    '''@return: e^i'''
    return math.exp(i)


@symbol('10^')
def pow10_op(i):
    '''@return: 10^i'''
    return 10 ** i


@symbol('^2')
def square_op(i):
    '''@return: i ** 2'''
    return i ** 2


@symbol('^3')
def cube_op(i):
    '''@return i ** 3'''
    return i ** 3


@symbol('Q')
def root_op(i):
    '''
    @return: square root of i
    @raise ValueError: invalid square root input
    '''
    return math.sqrt(i)


@symbol('Q3')
def cube_root_op(i):
    '''@return: cubed root of i'''
    return i ** (1./3)


@symbol('^-1')
def inverse_op(i):
    '''
    @return: 1. / i
    @raise ZeroDivisionError: i == 0
    '''
    return 1. / i


POWER_ARITY_1 = ln_op, log10_op, root_op, exp_op, pow10_op, square_op, \
                cube_op, inverse_op
POWER_ARITY_2 = power_op,
POWER_ALL = POWER_ARITY_1 + POWER_ARITY_2
