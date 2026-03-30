"""
Sol:
Key Idea:
Any subsequence that ends at i must come from somewhere before i.
So instead of checking all subsequences, we compute the best subsequence
ending at each index to find the best subsequence overall by taking max.

scan left -> extend valid subsequence -> choose longest valid subsequence

State:
dp[i] = length of the longest increasing subsequence that ends at index i

Recurrence: 
Look at all previous indices j before i, if any of its number is smaller 
than the number at index i, that means we can extend number at index i
onto the previous subsequence ending at j. 
dp[i] = 1 + max(dp[j]) if j < i and nums[j] < nums[i]


Base case:
The subsequence can end at each index with length of 1 just 1 number so
dp[i] = 1 for all i

Iteration Order:
we iterate from left to right as dp[i] depends on previous state

Final Answer:
max(dp[i]) for all i

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1) #find highest dp[j]
        
        return max(dp)
        