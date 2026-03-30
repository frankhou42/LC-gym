# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()
        
        #initialize queue
        q1.append(p)
        q2.append(q)

        #either queue empties we stop 
        while q1 or q2 :
            p = q1.popleft()
            q = q2.popleft()
            
            #check edge case first
            #reach end of tree continue checking other leaf nodes
            if not p and not q:
                continue
            #if one tree node is null and another is not return falase
            #if val not equal return false
            if (not p and q) or (not q and p) or p.val != q.val:
                return False
            
            #move on to the next layer
            q1.append(p.left)
            q1.append(p.right)
            q2.append(q.left)
            q2.append(q.right)
        
        return True
            

