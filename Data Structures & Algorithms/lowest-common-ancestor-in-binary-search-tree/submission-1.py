# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #look at three possible cases for a simple problem and expand
        #the simple solution using recursion

        #look at highlevel dont think too much! By just solving from
        #high level everything would make sense (need or not need helper func, return type, param etc)

        #consider case where p and q are both in same subtree, use that subtree as root,
        #continue to find lowest common ancestor in that subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            #return root on all other cases
            return root
       



    