from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    #how to traverse a linkedlist
    def traverse(self,head):
        cur = head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        print(first.val,second.val)
        return second
    def traverse(self,head):
        cur = head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()

#testing code
# head = ListNode(1)
# print(head.val)
# head.next = ListNode(2)
# print(head.next.val)
# head.next.next = ListNode(3)
# print(head.next.next.val)
# head.next.next.next = ListNode(4)
# print(head.next.next.next.val)
# linklist = ListNode()
# linklist.traverse(head)

# test = Solution()
# test.swapPairs(head)
# test.traverse(head)
# linklist.traverse(head)
# swapped = test.swapPairs(head)
# linklist.traverse(swapped)

#how to test swapPairs
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
linklist = ListNode()
linklist.traverse(head)
test = Solution()
swapped = test.swapPairs(head)
linklist.traverse(swapped)

