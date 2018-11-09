# pyOverloadedMethods
C style overloaded methods for Python. This is IDE safe (PyCharm tested)

Python 2.7+ compatible

This module needs 2 things to be done in order for it to work.
The class that you want to have overloaded methods in must be a subclass
of pyOverloadedMethods.OverloadedClass and the methods in which you
want to overload need to have identical name and have the decorator
@pyOverloadedMethods.overload

you are allowed to have positional arguments which do not have default
values overloaded arguments are keyword arguments with a default value
the type of the keyword values must match the default types. and all
keywords arguments MUST be used.

the ideal way is to set the default value to the type directly by using

    keyword=int()

this is the best way to be able to identify easily through your IDE
possible values that can be passed.

here is an example it is the same as what is found in example.py

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

My motivation for making this is I stumbled across this stackoverflow
post https://stackoverflow.com/questions/6434482/python-function-overloading
and it kind of got me in a frenzy and people stating it can't be done.
And that it will not function identical to how a C style overload works.

I also thought it would be damned handy to be able to separate code
based on what object types were passed into the method. and there is no
additional code of parsing kwargs for every single method you want to
"overload". Over 10000 calls it is about .65 seconds slower then doing a
bunch of isinstances. But if you have a slew of possible parameters
and keyword pairings it could end up being close to the same.

Python was never the roadrunner of languages. so for code simplicity
and ease of maintainability as well as adding to your code this might
be a worth while trade off.

This is also my first go at making this work. I am sure there is a much
cleaner and faster solution. if you have a way of making it better by
all means please do and submit a PR for it.
