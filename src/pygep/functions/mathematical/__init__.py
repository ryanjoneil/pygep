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
Provides basic arithmetic non-terminals for use in Chromosomes.
Any semantic exceptions (ZeroDivisionError, etc.) are passed up
the call chain to the user.  Typically one should catch any
exceptions when calling chromosome.evaluate() and set the fitness
of nonviable organisms to 0.

Provides pre-packaged GEP mathematics functions:
    - pygep.functions.mathematical.arithmetic
    - pygep.functions.mathematical.comparison
    - pygep.functions.mathematical.constants
    - pygep.functions.mathematical.hyperbolic
    - pygep.functions.mathematical.power
    - pygep.functions.mathematical.rounding
    - pygep.functions.mathematical.trigonometry
'''

from pygep.functions.mathematical.arithmetic import *
from pygep.functions.mathematical.comparison import *
from pygep.functions.mathematical.constants import *
from pygep.functions.mathematical.hyperbolic import *
from pygep.functions.mathematical.power import *
from pygep.functions.mathematical.rounding import *
from pygep.functions.mathematical.trigonometry import *


__all__ = 'MATH_ALL', 'MATH_ARITY_0', 'MATH_ARITY_1', 'MATH_ARITY_2'


MATH_ARITY_0 = CONSTANTS_ARITY_0
MATH_ARITY_1 = HYPERBOLIC_ARITY_1 + POWER_ARITY_1 + ROUNDING_ARITY_1 + \
               TRIGONOMETRY_ARITY_1
MATH_ARITY_2 = ARITHMETIC_ARITY_2 + COMPARISON_ARITY_2 + POWER_ARITY_2
MATH_ALL = MATH_ARITY_0 + MATH_ARITY_1 + MATH_ARITY_2
