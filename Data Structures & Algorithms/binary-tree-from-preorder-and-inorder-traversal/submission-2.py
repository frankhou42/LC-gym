"""
Key Insight:
Pre-order always gives the root.
In order divides the tree to left and right section. Helps with building right
and left subtree recursively

At any recursive call we only build the root node, the left and right subtree
is built with recursive calls

Inorder is important as it tells us mid index to partition the preorder and inorder arrays

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        #build entire left and right subtree
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[0 : mid])
        root.right = self.buildTree(preorder[mid + 1 : ], inorder[mid + 1 : ])

        return root
        
