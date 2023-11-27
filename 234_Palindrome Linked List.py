# Definition for singly-linked list.
import typing
import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: typing.Optional[ListNode]) -> bool:
        if head is None:
            return True
        if head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # slow is the middle
        # reverse the second half
        prev = None
        curr = slow.next
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # prev is the head of the second half
        # compare the first half and the second half
        while prev is not None:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

if __name__ == "__main__":

    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    test = Solution()
    test.isPalindrome(head)

