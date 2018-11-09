# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2018 EventGhost Project <http://eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
import timeit
from pyOverloadedMethods import OverloadedClass, overload

PRINT = True


class TestClass(OverloadedClass):

    @overload
    def test1(self, test1=int()):
        if PRINT:
            print('int called', test1)

    @overload
    def test1(self, test1=dict()):
        if PRINT:
            print('dict called', test1)

    @overload
    def test1(self, test1=float()):
        if PRINT:
            print('float called', test1)


t_class = TestClass()

t_class.test1(test1=1)
t_class.test1(test1=dict(test='test'))
t_class.test1(test1=1.45)

print(t_class.test1)

PRINT = False
COUNT = 0

code = '''
t_class.test1(test1=COUNT)
t_class.test1(test1=dict(test=COUNT))
t_class.test1(test1=0.45 + COUNT)
globals()['COUNT'] += 1
'''

test1 = timeit.timeit(code, number=10000, globals=locals())


class TestClass(object):

    def test1(self, test1):
        if isinstance(test1, int):
            if PRINT:
                print('int called', test1)

        if isinstance(test1, dict):
            if PRINT:
                print('dict called', test1)

        if isinstance(test1, float):
            if PRINT:
                print('float called', test1)


t_class = TestClass()

t_class.test1(test1=1)
t_class.test1(test1=dict(test='test'))
t_class.test1(test1=1.45)

COUNT = 0

test2 = timeit.timeit(code, number=10000, globals=locals())

print('test1:', test1)
print('test2:', test2)

print('overrides are slower by:', test1 - test2, 'over 10000 calls')
