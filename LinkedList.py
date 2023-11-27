"""
data structure : linkedlist and erchashu
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None  # None is object in Python


def build_linkedlist():
    print('build linked list')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    return node_1  # the head node of whole linkedlist can represent the whole linked list


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
