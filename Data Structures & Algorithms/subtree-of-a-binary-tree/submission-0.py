# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base cases
        #consider cases when null 
        if not root: return False
        if not subRoot: return True

        #Recursive case
        #if same tree at node return true
        if self.sameTree(root, subRoot):
            return True

        #check left and right subtree, if either is true we can return true for isSubtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        



    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base cases when just 2 nodes, it can be null or not
        if not subRoot and not root: 
            return True

        if not subRoot or not root:
            return False
        
        if subRoot.val != root.val:
            return False

        #recursive case consider when both nodes are equal
        return self.sameTree(root.right, subRoot.right) and self.sameTree(root.left, subRoot.left)
        

