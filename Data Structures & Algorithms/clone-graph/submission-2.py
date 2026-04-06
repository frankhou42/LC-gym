"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
copy tha value and its neightbors, then recursively process each neighbor
until we reach a node that we have already seen before
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}

        #copies the old graph to the new graph
        def dfs(node):
            #base case stop when seen b4, return the new node
            if node in oldToNew:
                return oldToNew[node]
            
            #add copy to  hashmap
            copy = Node(node.val)
            oldToNew[node] = copy

            #recursively copy neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)

