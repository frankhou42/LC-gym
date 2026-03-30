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
        #dummy node used cuz if n+1 may out of bounds,
        #use dummy node to advance to

        for _ in range(n): #must be n to make sure its in range
            r = r.next
        
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy.next

    #dummy node use cases:
    #Delete & Insertion at head
    #building/merging lists
    #we use dummy node to prevent writing special logic for first node