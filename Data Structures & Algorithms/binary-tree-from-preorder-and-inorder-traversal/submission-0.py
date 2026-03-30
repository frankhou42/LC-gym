# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #basecase, if either slice is None, we can't build the tree anymore as we have reach the end of tree
        if not preorder or not inorder:
            return None

        #preorder traversal first element always holds the root of subtree
        root = TreeNode(preorder[0])

        #index of the root in inorder traversal
        mid = inorder.index(preorder[0])

        #Now build left subtree
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        #preorder[1 : mid + 1] because exactly "mid" number of elements
        #are in the left subtree if we look at the tree structure in the inorder arr

        #notice! sequence[start : stop] index go up to stop but doesn't include stop
        #so for preorder[1 : mid + 1] we would get mid elemetns since 1 to mid

        #Build right subtree
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        #function returns a fully built subtree
        return root
