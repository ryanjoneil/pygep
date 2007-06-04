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
Common trigonometric functions:
    - (sin) sine_op:      math.sin(x)
    - (cos) cosine_op:    math.cos(x)
    - (tan) tangent_op:   math.tan(x)
    - (csc) cosecant_op:  1 / math.sin(x)
    - (sec) secant_op:    1 / math.cos(x)
    - (cot) cotangent_op: 1 / math.tan(x)
'''

# TODO: inverse functions

from pygep.chromosome import symbol
import math


__all__ = 'TRIGONOMETRY_ALL', 'TRIGONOMETRY_ARITY_1'


@symbol('sin')
def sine_op(i):
    '''@return: math.sin(i)'''
    return math.sin(i)


@symbol('cos')
def cosine_op(i):
    '''@return: math.cos(i)'''
    return math.cos(i)


@symbol('tan')
def tangent_op(i):
    '''@return: math.tan(i)'''
    return math.tan(i)


@symbol('csc')
def cosecant_op(i):
    '''@return: 1. / math.sin(i)'''
    return 1. / math.sin(i)


@symbol('sec')
def secant_op(i):
    '''@return: 1. / math.cos(i)'''
    return 1. / math.cos(i)


@symbol('cot')
def cotangent_op(i):
    '''@return: 1. / math.tan(i)'''
    return 1. / math.tan(i)


TRIGONOMETRY_ARITY_1 = sine_op, cosine_op, tangent_op, cosecant_op, \
                       secant_op, cotangent_op
TRIGONOMETRY_ALL = TRIGONOMETRY_ARITY_1
