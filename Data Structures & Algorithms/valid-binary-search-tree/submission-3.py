"""
Key Insight:
Every node must fit within a valid value range decided by all its ancestor
Since we need a range based on parent we make helper dfs with added input param
for lowest and largest 

We tighten the bounds as we go to left subtree we change right bound, right subtree
left bound.

purpose of dfs is to return boolean checking if a subtree is valid or not
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, lowest, largest):
            if not node:
                return True
            
            if lowest < node.val and largest > node.val:
                return valid(node.left, lowest, node.val) and valid(node.right, node.val, largest)
            else:
                return False
        
        return valid(root, float('-inf'), float('inf'))
        


