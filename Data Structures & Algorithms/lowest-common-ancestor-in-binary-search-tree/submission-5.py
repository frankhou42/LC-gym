"""
The tree is BST, if p and q are smaller than currNode, p and q are on left subtree
otherwise, right subtree. If every other case of p and q relation with currNode, we
are currently at the LCA. We do this currNode for every single node with dfs
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #base case
        if root.val == p.val:
            return p

        if root.val == q.val:
            return q 
        #recursive case
        if p.val < root.val and q.val > root.val or p.val > root.val and q.val < root.val:
            return root
    
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

