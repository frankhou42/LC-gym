# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = None
        def dfs(node):
            nonlocal cnt, res
            #base case stop recursion if reach the end of tree
            #or if the res value already updated
            if not node or res:
                return 
            
            #check left subtree if it has the node
            dfs(node.left)


            #process curr node
            cnt -= 1
            if cnt == 0:
                res = node.val


            dfs(node.right)
        
        dfs(root)
        return res