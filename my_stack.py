# stack: first in last out []
"""
push(value)
pop()
peek()
is_empty()
size()

since there is no stack in python, we can use list to implement stack
the end of the list is the top of the stack
we can visit any element in the list, so we can use list to implement stack, queue, deque but we can't use list to implement priority queue, can't use list to implement heap, because we can't visit any element in the list
While we can use list to implement stack, queue, deque, but it's not efficient, because list is a dynamic array, it's not a linked list, so it's not efficient to insert or delete element in the middle of the list
We can not visit any element in the stack, we can only visit the top of the stack, so we can use linked list to implement stack, queue, deque, priority queue, heap
"""


class MyStack():
    # use list
    def __init__(self):
        self.items = []  # this attribute is a list

    def is_empty(self):
        return not self.items  # return len(self.items) == 0

    def push(self, item):
        self.items.append(item)  # why this one doesn't have return value? because we don't need to return anything

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    my_stack = MyStack()  #create an object my_stack
    for i in range(50):
        my_stack.push(i) # push 0 to 49 into the stack

    while not my_stack.is_empty():
        print(my_stack.pop(), end=' ')
    print()  # 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
