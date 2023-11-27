# Description: This program demonstrates the call stack in Python.
# The call stack is a stack data structure that stores information about the active subroutines of a computer program.
# This kind of stack is also known as an execution stack, program stack, control stack, run-time stack, or machine stack,
# and is often shortened to just "the stack".
# in OS, the stack is used to store the return address of the function, the parameters of the function, and the local variables of the function.
# stackoverflow means the stack is full, and the program will crash. call, return function 
def main():
    num = 10
    print(num)
    foo()
def foo():
    name = 'abc'
    print(name)
    bar()
def bar():
    baz()
    arr = [1,2,3]
    for num in arr:
        print(num)
def baz():
    print('I am baz function')

if __name__ == '__main__':
    main()