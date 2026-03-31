"""
Key Insight:
We pass extra parameters into DFS when we need information from the parent,
and we return values from DFS when we need information from the children.


Recursive Case:
if node.val is bigger than max then its goodNode, if smaller then we pass

purpose of dfs is to pass on the maximum downwards to the path and go through
every node
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goods = 0
        def dfs(node, maximum):
            #base case
            if not node:
                return
            
            #recursive case
            if node.val >= maximum:
                self.goods += 1
                maximum = max(node.val, maximum)
            
            #pass on the maximum downwards to the path
            dfs(node.left, maximum)
            dfs(node.right, maximum)
        
        dfs(root, root.val)

        return self.goods
                

