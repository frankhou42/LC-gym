"""
We want to iterate through each node and find its left and right
subtree height to find max length
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

        #dfs gives height of node
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
        
