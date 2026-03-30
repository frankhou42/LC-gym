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
        #avoid cases when the curr ptr points to None is line26,27 causing keyError
        #as the key of hashmap can't be none
        hashmap = {None : None}
        
        #first pass create each node map for the oldtonew hashmap
        curr = head
        while curr:
            #can't assign curr.next to copy's next
            hashmap[curr] = Node(curr.val)
            curr = curr.next

        #second pass create the links for random since some links has huge jumps
        curr = head
        while curr:
            #random needs to be mapped to the copy node
            hashmap[curr].random = hashmap[curr.random]
            hashmap[curr].next = hashmap[curr.next]
            curr = curr.next

        return hashmap[head]


