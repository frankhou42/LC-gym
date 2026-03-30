# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Pre order traversal
        #base case
        if not root:
            return None
        
        #swap left and right
        root.left, root.right = root.right, root.left

        #Trust the invert function call
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

