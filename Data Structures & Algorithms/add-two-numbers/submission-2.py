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
        while l1 and l2:
            total = (l1.val + l2.val + remainder) % 10
            remainder = (l1.val + l2.val) // 10
            curr.next = ListNode(total)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        rest = l1 if l1 else l2

        while rest:
            total = (rest.val + remainder) % 10
            remainder = (rest.val + remainder) // 10
            curr.next = ListNode(total)
            curr = curr.next
            rest = rest.next
        
        if remainder > 0:
            curr.next = ListNode(remainder)
        
        return dummy.next



