# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #when creating a new LL use a dummy node to avoid edge cases near head
        dummy = ListNode()
        #tail is a ptr that 
        tail = dummy
        #if list1 or list2 is ptr to a null (aka ptr to null of LL), we stop
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
        
            #advance tail ptr!!!!!!
            tail = tail.next
        
        #append the none null list to the tail
        tail.next = list1 or list2

        return dummy.next



