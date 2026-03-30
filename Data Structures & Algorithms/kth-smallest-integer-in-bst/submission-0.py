# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = k
        self.res = None
        def dfs(node):
            #base case stop recursion if reach the end of tree
            #or if the res value already updated
            if not node:
                return 
            
            #check left subtree if it has the node
            dfs(node.left)
            #Early return
            if self.res:
                return

            #process curr node
            self.cnt -= 1
            if self.cnt == 0:
                self.res = node.val
                #Early return
                return

            dfs(node.right)
        
        dfs(root)
        return self.res