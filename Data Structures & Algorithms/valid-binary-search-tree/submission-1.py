# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #need updated LBound and RBound in each stage to see node validity
        def validBST(LBound, node, RBound) -> bool:
            #base case
            if not node: 
                return True

            #Check if in bound
            if not LBound < node.val < RBound:
                return False

            #update LBound and RBound recursively, check if left and right subtree are valid
            return validBST(LBound, node.left, node.val) and validBST(node.val, node.right, RBound)

        return validBST(float("-inf"), root, float("inf"))