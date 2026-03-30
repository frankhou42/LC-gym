# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []

        if not root:
            return []

        #we want to process every node, when everything processed q empty
        while q:
            #iterate through each node in the layer
            length = len(q)
            res.append(q[-1].val)
            for _ in range(length):
                #node we are processing
                node = q.popleft()
                #add node nei, remove node
                #!important: check left and right null before append
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res
