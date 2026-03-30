class Solution:
    def climbStairs(self, n: int) -> int:
        #!!! 0 based indexing requires n + 1 to be able to index to n
        dp = [0] * (n + 1)
        #base cases here
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1): # iterated till n
            #store opt(i) in dp arr
            dp[i] = dp[i - 1] + dp[i - 2]

        #res at last index
        return dp[n]