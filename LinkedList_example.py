# coding=utf-8

# how to build linked list
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None  #Object, when you don't know the value, placehold it with None

#node_1 --> None--> node_2 --> None --> node_3 --> None -->node_4 --> None
#node_1 --> node_2 --> node_3 --> node_4 --> None
#copy node_2 address to node_1.next
#Object node_1's attribute next is a pointer to another object node_2
def build_linkedlist():
    print('Build linked list')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    return node_1 #head node represents the whole linked list


def run_linkedlist_example():
    print('LinkedList example')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    cur = node_1
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print('\n')


def run_linkedlist_quiz_1():
    print('LinkedList quiz 1')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    node_2 = node_3 # node_2 and node_3 are both pointing to the same object 5, as long as node.next is not changed, the linked list is not changed

    cur = node_1
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print('\n')


def run_linkedlist_quiz_2():
    print('LinkedList quiz 2')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    #a = node_1 # a is pointing to the object 1
    node_1 = node_2 # node_1 and node_2 are both pointing to the same object 3

    cur = node_1 # node_1 is the head node
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print('\n')


def run_linkedlist_quiz_3():
    print('LinkedList quiz 3')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    node_1.next = node_3 # node_1.next is changed to node_3, node_2 is not pointing to any object, so it is garbage collected

    cur = node_1
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next
    print('\n')


if __name__ == '__main__':
    run_linkedlist_quiz_1() # 1 3 5 7 node_2 and node_3 are both pointing to the same object 5
    run_linkedlist_quiz_2() # 3 5 7 node_1 and node_2 are both pointing to the same object 3, object 1 is garbage collected(no reference), memory released
    run_linkedlist_quiz_3() # 1 5 7 node_1.next is changed to node_3, node_2 is not pointing to any object, so it is garbage collected
