"""
Sol:
We need to keep track of the state of min and max product subarray ending
at index i using 2 dp arrs

We do this because negative nums[i] can flip the sign making min to become max

At each index we update both values by taking max/min of:
    - starting a new subarr from i by making nums[i] new max or min
    - extending previous max/min by multiplying nums[i] to update max/min arr

We keep track of the global maximum across all and return it as final answer

Note: state means dp[i]

Since non-empty, dp states are 1...n arrs are len(nums)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        min_dp = [0] * n
        max_dp = [0] * n

        #base cases
        min_dp[0] = nums[0]
        max_dp[0] = nums[0]

        #global max
        res = nums[0]

        for i in range(1, n):
            #max of (start new, extend min, extend max), 3 choices
            max_dp[i] = max(nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i])
            min_dp[i] = min(nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i])


            #check for each subarray if their product is bigger than res 
            res = max(res, max_dp[i])
        return res


        