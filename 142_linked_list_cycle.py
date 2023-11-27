import typing

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: typing.Optional[ListNode]) -> typing.Optional[ListNode]:
        if head is None:
            return None
        
        slow = head
        fast = head
        hasCycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break
        
        if not hasCycle:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

    
if __name__ == '__main__':
    test = Solution()
    print(test.detectCycle([3,2,0,-4]))
    print(test.detectCycle([1,2]))
    print(test.detectCycle([1]))
    print(test.detectCycle([]))