# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        tail = dummy
        curr1 = list1
        curr2 = list2
        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2 #not the val the ndoe is to be attached
                curr2 = curr2.next
            
            tail = tail.next
        
        tail.next = curr1 or curr2

        return dummy.next
            
        
        
