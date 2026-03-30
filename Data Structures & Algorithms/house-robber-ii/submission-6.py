"""
approach from macro perspective, getting multiple dp[i]s for different nums and get max
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        #need to check edge case outside function too incase input is jsut len 1
        if len(nums) == 1:
            return nums[0]

        def rob_lines(nums):
            #edge case, when there is only one house the dp doesn't apply
            if len(nums) == 1:
                return nums[0]
            # dp[i] is the max amount of money we can rob from 1 to ith house
            # There are n number of states
            n = len(nums)
            dp = [0] * n
            #1 based index, there are n houses total
            #dp = 1...n

            #recurrence relation -> dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            #base cases
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
                #dp is 1 based index, nums is 0 based index, therefore we decrement nums by 1 
                #since nums is one more than dp
            return dp[n - 1]
        
        return max(rob_lines(nums[:-1]), rob_lines(nums[1:]))
