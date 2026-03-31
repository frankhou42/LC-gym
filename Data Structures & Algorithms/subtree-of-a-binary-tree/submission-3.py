"""
go through each node in root, if there is at a node the rest matches subRoot
then return true, if not check if subTree is in left or right subtree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            
            if isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right) and t1.val == t2.val:
                return True
            else:
                return False

        #base case
        if not root:
            return False
        
        if not subRoot:
            return True
    
        #recursive case
        if isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
#time O(n * m) where n is number of nodes in root and m is for subRoot, 
#space O(h + h) since we go down 2 paths maximum 

        
        