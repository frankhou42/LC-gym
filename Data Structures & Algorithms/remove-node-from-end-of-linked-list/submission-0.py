# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #use the two ptrs technique
        dummy = ListNode(0, head)
        l = dummy
        r = head

        for _ in range(n): #must be n to make sure its in range
            r = r.next
        
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy.next
