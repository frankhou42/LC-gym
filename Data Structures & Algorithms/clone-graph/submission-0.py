"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}

        if not node:
            return None
        
        #input root node of old graph, return its corresponding newNode if visited
        #after each recursive call return also return corresponding newNode

        def dfs(node):
            #base case: when node already visited, return the visited new node
            if node in oldToNew:
                #to append newNode as a neighbor to another newNode
                return oldToNew[node]

            #for each node first create a copy
            newNode = Node(node.val)
            #map old node with new node
            oldToNew[node] = newNode
            
            #append neighbors of old to new
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))
            
            #return new node so that prev call
            return oldToNew[node]

        #in the end return the root of new node
        return dfs(node)
            

            