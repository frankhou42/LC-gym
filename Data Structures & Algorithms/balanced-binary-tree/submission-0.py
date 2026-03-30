# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #use dfs to find the depth of left and right
        #if abs(leftD - rightD) < 1 return true and the depth
        def dfs(node: Optional[TreeNode]) -> [bool, int]:
            if not node:
                return [True, 0]
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            if abs(leftHeight[1] - rightHeight[1]) <= 1 and leftHeight[0] and rightHeight[0]:
                return [True, 1 + max(leftHeight[1], rightHeight[1])]
            else:
                return [False, 0]
        

        return dfs(root)[0]

        
