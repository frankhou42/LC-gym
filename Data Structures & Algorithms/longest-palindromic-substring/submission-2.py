"""
Sol:

Go through every single substring, find every single possible
pali and update the res (holds longest)

dp[l][r] 2D DP since there are nxn states

At each problem state we check if its pali with s[l] == s[r],
if subproblem dp[l+1][r-1] is pali (dp), and if r - l <= 2 
(base case).

Since l+1 and r-1 is subproblem we iterate right to left for l,
left to right for r so that subproblem would have been computed
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        #2d dp
        dp = [[False] * n for _ in range(n)]

        res = ""

        for l in range(n - 1, -1, -1):
            for r in range(l, n): #l == r one character is also a substring
                if (r - l <= 2 and s[l] == s[r]) or (dp[l + 1][r - 1] and s[l] == s[r]):
                    #need to update dp table
                    dp[l][r] = True

                    if len(res) < len(s[l : r + 1]): # +1 for python syntax
                        res = s[l : r + 1]
                    
                

        return res


        