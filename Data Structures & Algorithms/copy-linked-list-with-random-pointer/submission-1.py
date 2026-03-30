"""
We use dummy node so that every node has a previous node
This helps with cases like deleting nodes, inserting nodes, 
skipping nodes, builidng new lists.

key is old LL, val is new LL

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #need a None : None pair for the last element None for both LL
        oldToNew = {None : None}
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            oldToNew[curr].next = oldToNew[curr.next]
            oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]

            