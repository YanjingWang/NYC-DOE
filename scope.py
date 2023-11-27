"""
local: variables defined within a function
enclosing: variables in the local scope of enclosing functions
global: declared in this module or explicitly declared global using the global
built-ins : names are preassigned in Python
"""

x = 'global x'


def test():
    global x  # overriding values of function variable
    x = 'local x'
    # print(y)
    print(x)


test()
print(x)


def test_z(z):
    x = 'local x'
    # print(y)
    print(z)


test_z('local z')

m = min([5, 1, 4, 2, 3])
print(m)

import builtins

print(dir(builtins))


def min():
    pass


# n = min([99, 94, 888, 56, 79])
# print(n)  # find min() in build-in instead of global scope

"""
the enclosing has to do with nested functions
"""


def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)  # enclosing scope

    inner()
    print(x)


outer()
print(x)

"""

"""


def outer():
    x = 'outer x'

    def inner():
        nonlocal x  # nonlocal statement
        x = 'inner x'
        print(x)  # enclosing scope, used to change the state of closures and decorators

    inner()
    print(x)  # inner x


outer()
print(x)  # inner x
