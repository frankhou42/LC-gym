# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #class-wise global var, mutable in helper
        self.res = 0

        def dfs(node: Optional[TreeNode]) -> int:
            #base case
            if not node:
                return False
            
            #find the depth of right and left, trust the func
            left = dfs(node.left)
            right = dfs(node.right)

            #diameter (longest path) gets updated
            self.res = max(self.res, left + right)

            #return to previous func call the dfs (the purpose of this function,
            #deepest node) of current node layer
            return max(left, right) + 1

            #e.g: at node 2, L=2 R=1 res=L+R=3. Then the res
            #gets updated to 
            
        dfs(root)
        return self.res
