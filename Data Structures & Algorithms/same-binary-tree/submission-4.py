"""
Key Insight:
- DFS is just a way of traversing graph
- consider all base cases. For here consider when one 
has node and one doesn't

do dfs across p and q simulatenously check same left and 
right sub tree and curr node
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False
        
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val:
            return True
        else:
            return False
