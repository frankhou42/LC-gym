# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS
        res = []
        q = collections.deque()
        q.append(root)
        #consider the case where tree is null
        if not root:
            return[]

        #keep operating till q is empty
        while q:
            qLen = len(q)
            #first append the value of most right in a layer
            res.append(q[qLen - 1].val)

            for element in range(qLen):
                #pop an element from the left and append its left
                #and right child to the queue when not null
                node = q.popleft()
                #ensure we are not adding null elements to q
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                        
        return res

            


