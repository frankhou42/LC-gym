# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root):

        #Creates a class-wide attribute for only the instance
        #temporarily for this func
        self.count = 0

        def dfs_addGoodNodes(node, maxVal) -> None:
            if not node:
                return None
            
            #decide if the node is valid, if so add to total count
            if node.val >= maxVal:
                maxVal = node.val
                self.count += 1
            
            #recursively add nodes from left and right subtree from node
            dfs_addGoodNodes(node.left, maxVal)
            dfs_addGoodNodes(node.right,maxVal)
            
        dfs_addGoodNodes(root, root.val)
        #since start at root, the maxval will be the root's value

        return self.count
