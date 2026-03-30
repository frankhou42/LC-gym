# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case, when the algo ends
        if not root:
            return None

        #invert left and right
        root.left, root.right = root.right, root.left

        #go invert left and right branch
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
