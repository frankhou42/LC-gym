"""
Find height of left and right subtree recursively and then compare the 
height, if > 1 then return false, else true

We use nested dfs to to solve the subproblem of height
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            #subtree and currNode balanced
            if abs(left[1] - right[1]) <= 1 and left[0] and right[0]:
                return [True, 1 + max(left[1], right[1])]
            else:
                return [False, 1 + max(left[1], right[1])]


        return dfs(root)[0]


            
