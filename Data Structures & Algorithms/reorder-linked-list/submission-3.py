"""
Reverse the second half to simulate backward traversal, 
then merge the first half and reversed second half by 
changing nodes pointers in-place.
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
        #we stop when second is empty because by then
        #all interleaving is complete and leftover first
        #nodes are in place
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
            

        

        