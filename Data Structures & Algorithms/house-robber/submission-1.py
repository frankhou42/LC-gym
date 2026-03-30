class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] is the max amount of money we can rob at ith house
        # There are n number of states
        n = len(nums)
        dp = [0] * (n + 1)
        #0 based index, there are n houses total but we also consider 0 houses
        #dp = 0...n

        #recurrence relation -> dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        #base cases
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])
            #dp is 1 based index, nums is 0 based index, therefore we decrement nums by 1 
            #since nums is one more than dp
        return dp[n]
