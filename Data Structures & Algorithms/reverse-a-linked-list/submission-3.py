"""
When we try to reverse a link, we realize we lose the rest of
the LL, so we use a tmp varaible to save the rest of the LL during
reversal

After reversing, when we move on with the LL we realize we
need the past element so we use a prev ptr to track it

From there we form a loop where we save the next section of LL
and use prev ptr to reverse with curr and advance both pointers 
until curr reaches None
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            #save
            tmp = curr.next
            #reverse
            curr.next = prev
            #advance ptrs
            prev = curr
            curr = tmp

        #return head of new LL
        return prev
            
            
