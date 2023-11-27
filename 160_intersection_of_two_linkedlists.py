import typing
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> typing.Optional[ListNode]:
        if not headA or not headB:
            return None
        p1, p2 = headA, headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1
    
test = Solution()
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)
headB = ListNode(5)
headB.next = ListNode(0)
headB.next.next = ListNode(1)
headB.next.next.next = headA.next.next
print(test.getIntersectionNode(headA, headB).val)

