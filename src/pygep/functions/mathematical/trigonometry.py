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
    - (SIN ) sine_op:         math.sin(x)
    - (COS ) cosine_op:       math.cos(x)
    - (TAN ) tangent_op:      math.tan(x)
    - (CSC ) cosecant_op:     1 / math.sin(x)
    - (SEC ) secant_op:       1 / math.cos(x)
    - (COT ) cotangent_op:    1 / math.tan(x)
    - (ASIN) arcsine_op:      math.asin(x)
    - (ACOS) arccosine_op:    math.acos(x)
    - (ATAN) arctangent_op:   math.atan(x)
    - (ACSC) arccosecant_op:  1 / math.asin(x)
    - (ASEC) arcsecant_op:    1 / math.acos(x)
    - (ACOT) arccotangent_op: 1 / math.atan(x)
'''

from pygep.chromosome import symbol
import math


__all__ = 'TRIGONOMETRY_ALL', 'TRIGONOMETRY_ARITY_1'


sine_op         = symbol('SIN' )(lambda i: math.sin(i))
cosine_op       = symbol('COS' )(lambda i: math.cos(i))
tangent_op      = symbol('TAN' )(lambda i: math.tan(i))
cosecant_op     = symbol('CSC' )(lambda i: 1. / math.sin(i))
secant_op       = symbol('SEC' )(lambda i: 1. / math.cos(i))
cotangent_op    = symbol('COT' )(lambda i: 1. / math.tan(i))
arcsine_op      = symbol('ASIN')(lambda i: math.asin(i))
arccosine_op    = symbol('ACOS')(lambda i: math.acos(i))
arctangent_op   = symbol('ATAN')(lambda i: math.atan(i))
arccosecant_op  = symbol('ACSC')(lambda i: 1. / math.asin(i))
arcsecant_op    = symbol('ASEC')(lambda i: 1. / math.acos(i))
arccotangent_op = symbol('ACOT')(lambda i: 1. / math.atan(i))


TRIGONOMETRY_ARITY_1 = sine_op, cosine_op, tangent_op, cosecant_op, \
                       secant_op, cotangent_op, arcsine_op, arccosine_op, \
                       arctangent_op, arccosecant_op, arcsecant_op, \
                       arccotangent_op
TRIGONOMETRY_ALL = TRIGONOMETRY_ARITY_1
