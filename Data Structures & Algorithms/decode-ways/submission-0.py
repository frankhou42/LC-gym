"""
Thoery:
dp is just recursive brute force done iteratively with cache

Top down -> start with original problem and recursively break
it down to smaller subproblems, if solved, cache to avoid repeated
computation

Bottom up -> start with smallest subproblem and incrementaly build
to get to complex final problem 

Both can be used

For size of DP arr, if dp need to represent empty state len is n + 1, 
else n

Sol:
dp[i] = number of ways to decode up to index i

At each index, we can:
- take 1 digit (if valid) → extend all ways from dp[i-1]
- take 2 digits (if valid) → extend all ways from dp[i-2]

We combine results instead of adding 1 because each valid choice
extends multiple previous decoding paths, creating multiple new ways.

eg. 22
At index 1 we can either extend "2" or "22", 
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
            
        n = len(s)
        dp = [0] * (n + 1)
        
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            #valid with taking 1 char
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            #valid with taking 2 chars
            if int(s[i - 2: i]) <= 26 and s[i - 2] != "0":
                dp[i] += dp[i - 2]
        
        return dp[n]


