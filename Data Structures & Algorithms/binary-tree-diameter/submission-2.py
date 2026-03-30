"""
We want to find the height of each node so that we can use
that height of left and right subtree to update diameter
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #we can still add global variable in class in functions
        self.longestPath = 0

        def dfs(node):
            #base case
            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            
            #Update
            self.longestPath = max(leftHeight + rightHeight, self.longestPath)

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return self.longestPath
        
