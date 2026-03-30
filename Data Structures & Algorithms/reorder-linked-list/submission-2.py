"""
intuitively we are taking one from front and on from back
to do this we can just reverse the second half secton of LL
and have two LLs

we do so with slow and fast ptr

we iterate through the two LLs and construct LL in-place
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #fast at head.next so that we are 1 element
        #before second half to set the end of first half
        #and end of second half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        second = slow.next
        slow.next = None
        prev = None
        #keep iterating until we reach edn of second
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
            

        

        