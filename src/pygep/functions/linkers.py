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
Provides linkers for combining multigenic chromosomes.  In general
PyGEP linkers should accept and process any number of arguments,
thus the use of *args.

Most common linkers:
    - default_linker: returns tuple or ET results, or single result for 1 gene
    - sum_linker:     equivalent to sigma.  Sums results of sub-ETs.
    - or_linker:      boolean OR of results of sub-ETs
'''


__all__ = 'default_linker', 'sum_linker', 'or_linker'


def default_linker(*args):
    '''@return: either a single value or a tuple, depending on context'''
    if len(args) == 1:
        return args[0]
    return args


def sum_linker(*args):
    '''@return: the sum of all sub-ETs'''
    return sum(args)


def or_linker(*args):
    '''@return: the OR of all given args'''
    for arg in args:
        if arg:
            return True
    return False
