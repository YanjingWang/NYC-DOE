# Definition for singly-linked list.
import typing
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: typing.Optional[ListNode]) -> typing.Optional[ListNode]:
        if not head:
            return None
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
    
    
if __name__ == "__main__":
    test = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    print(test.reverseList(head)) # 3->2->1->None
    head = ListNode(1)
    print(test.reverseList(head)) # 1->None
    head = None
    print(test.reverseList(head)) # None
    head = ListNode(1)
    head.next = ListNode(2)
    print(test.reverseList(head)) # 2->1->None