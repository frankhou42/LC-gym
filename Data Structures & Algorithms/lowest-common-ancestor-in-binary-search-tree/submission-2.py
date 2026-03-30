# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #iterative solution, space complexity O(1) because linear func call stack (func called once)
        #and no extra DS

        curr = root
        
        #start from root iterate down the tree to find LCA (Lowest Common Ancestor)
        while curr:
            #if both p and q in same subtree keep traversing
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
