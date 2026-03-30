class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()#Tip: syntax for a intiatilizing a queue
        l = r = 0

        for r in range(len(nums)):
            #keep poping the smallest elements in queue
            #to make sure in descending order
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            #enqueue new index
            q.append(r)

            #pop elements lefter than the leftest index of window
            if l > q[0]:
                q.popleft()

            #we have finished initializing the first window and is sliding
            if (r + 1) >= k:
                #we start to add the largest num which is at the leftest of queue
                res.append(nums[q[0]])
                l += 1

        
        return res


