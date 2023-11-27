# coding=utf-8


class ListNode:
    #constructor: define a node instance
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None # as long as head node is known, the whole linked list is known

    def get(self, location):
        cur = self.head
        for i in range(location):
            cur = cur.next
        return cur.val

# add a new node after the node at the given location
# if location is 0, add a new node before the head node
#list = [1, 3, 5, 7] add 2 at location 2
# new_node.next = pre.next
# pre.next = new_node
    def add(self, location, val):
        if location > 0:
            pre = self.head
            for i in range(location - 1): # pre is the node at location - 1
                pre = pre.next  # hard to understand
            new_node = ListNode(val)
            new_node.next = pre.next
            pre.next = new_node
        elif location == 0:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head = new_node

    def set(self, location, val):
        cur = self.head
        for i in range(location):
            cur = cur.next
        cur.val = val

    def remove(self, location):
        if location > 0:
            pre = self.head
            for i in range(location - 1):
                pre = pre.next

            pre.next = pre.next.next

        elif location == 0:
            self.head = self.head.next

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()

    def is_empty(self):
        return self.head is None


if __name__ == '__main__':
    ll = MyLinkedList()
    ll.add(0, 1)
    ll.add(1, 3)
    ll.add(2, 5)
    ll.add(3, 7)
    ll.traverse()

    ll.add(0, 9)
    ll.add(1, 100)
    ll.traverse()

    print(ll.get(1))  # 100
    print(ll.get(3))  # 3

    ll.set(0, -100)
    ll.set(2, 32)
    ll.traverse()

    ll.remove(2)
    ll.traverse()
