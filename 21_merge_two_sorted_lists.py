# Definition for singly-linked list.
import typing
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1 is None:
#             return list2
#         elif list2 is None:
#             return list1
#         elif list1.val < list2.val:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         else:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2
#
# #how to test this code?
# # nums = [2, 7, 11, 15]
# # target = 9


class Solution:
    def mergeTwoLists(self, list1: typing.Optional[ListNode], list2: typing.Optional[ListNode]) -> typing.Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next

            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        return dummy.next
    
# test code
# list1 = [1,2,4]
# list2 = [1,3,4]
# print(Solution().mergeTwoLists(list1, list2))


list1 = [1,2,4]
list2 = [1,3,4]
# listnode1 = 
input1 = Solution()
input1.mergeTwoLists(list1, list2)

