# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #maxDepth requires postorder traversal where we needs to first
        #recurse on the children then combine children results a

        #base case
        if not root:
            return 0

        #Inductive case: use same function on smaller inputs and combine
        #answers

        #Contract Mentality
        #assume maxDepth already knows how to get the correct depth,
        #write out the general pattern

        #get left and right depth then add 1 for root
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        return 1 + max(leftMax, rightMax)
        
        