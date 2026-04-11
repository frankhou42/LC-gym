"""
Key Insight:
we use dfs to traverse the graph, going through every single
connection to make copy. Since cycle can appear as we traverse 
the graph, we use hashmap to keep track of visited(copied) nodes
to prevent recreating same nodes.

!!!If we need a global var, we need to create helper dfs functions
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        hashmap = {}
        
        #Purpose: copy graph and then return copied version of curr node
        def dfs(node):
            #base case
            if node in hashmap:
                return hashmap[node]
            
            #recursive case
            hashmap[node] = Node(node.val)
            for nei in node.neighbors:
                hashmap[node].neighbors.append(dfs(nei))

            #return copied version of curr node
            return hashmap[node]

        return dfs(node)







                