# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        #safety check to see if fast ptr can progress
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        #if there is a cycle the fast ptr will eventually meet slow ptr as their distance
        #gets closed by 1 each loop. if not run off the LL