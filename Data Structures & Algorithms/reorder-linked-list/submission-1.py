# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #use fast and slow pointer to have slow at mid of LL
        slow, fast = head, head.next # fast
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #break the LL to half, reverse the second linklist
        second = slow.next
        slow.next = None #end the second half of LL
        #reverse LL
        prev = None
        while second: #the second half is smaller, so we do this while we have second half
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        #In the end curr is none and prev is the new head of reversed LL

        #merge the reversed second LL and the origina first LL
        first, second = head, prev
        while first and second: #
            tmp1, tmp2 = first.next, second.next
            #connect ptrs of one iteration
            first.next = second
            second.next = tmp1
            #now advance ptrs
            first, second = tmp1, tmp2
        

            



        
