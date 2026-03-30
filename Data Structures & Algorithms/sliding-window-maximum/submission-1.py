class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()#Tip: syntax for a intiatilizing a queue
        l = r = 0

        while r < len(nums):
            #keep poping the smallest elements in queue until we only have elements greater
            #and equal to the number we are going to add
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            #pop elements lefter than the leftest indexx of window
            if l > q[0]:
                q.popleft()

            #we have finished initializing the first window and is sliding
            if (r + 1) >= k:
                #add the largest num which is at the leftest of queue
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res