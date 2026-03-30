# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        stack = [] 
        #holds all the parents while traversing left subtree, will be revisited
        #when poped as it holds the node from bottom to tom (dfs)
        curr = root #ptr to hold the node that we are processing

        #continue traversing the tree if either not at the end of tree or
        #there are nodes left to visit
        while curr or stack:
            #go to leftest subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            #process the node
            curr = stack.pop()
            cnt -= 1
            if cnt == 0:
                return curr.val
            
            #go to right subtree of each node
            curr = curr.right



