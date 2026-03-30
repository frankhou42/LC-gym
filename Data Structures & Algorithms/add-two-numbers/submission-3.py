"""
Key Optimization with One Pass:
if l1 or l2 depleted we don't keep going we stick to none and let
value be 0. We also continue the loop if remainder exists at the end
adding to to the LL
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or remainder:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = (val1 + val2 + remainder) % 10
            remainder = (val1 + val2 + remainder) // 10
            curr.next = ListNode(total)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next



