"""
two LLs, compare LL node vals, to decide which node val to append
to new LL and advance. if one LL runs out just append the rest
of the other to new LL

dummy.next reserved for return, use curr to iterate and build
the new LL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            
            #advance new LL ptr
            curr = curr.next

        curr.next = list1 if list1 else list2

        
        return dummy.next