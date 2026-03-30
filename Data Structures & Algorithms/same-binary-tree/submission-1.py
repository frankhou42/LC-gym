# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case since it checks curr node and stops recursion
        #quitting layers of the dfs call stack
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        #if func is in a class, call self
        leftRes = self.isSameTree(p.left, q.left)
        rightRes = self.isSameTree(p.right, q.right)

        #subproblem: if both left and right subtrees are the same at root then the tree is the same
        return leftRes and rightRes

            