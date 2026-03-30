"""
dp entries dont store the final answer but partial answer/final answer.
The partial answers to subproblems would help to build the final answer

go through every single possible substring and check if its pali
with recurrence and base case if its pali add to counter, else
passs.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        #dp[l][r] means for given l & r is it pali
        #the options of subproblem are:
        # dp[l+1][r-1] is also a pali and s[l] == s[r]
        # dp[l+1][r-1] is not a pali or s[l] != s[r]

        res = 0
        #pali counter

        #we need to have the next left and the prev right, so for l
        #we loop from right to left and r left to right
        for l in range(n - 1, -1, -1):
            for r in range(l, n): #l & r can be the same ptr
                #base case or recurrence, we count once
                if (r - l <= 2 and s[l] == s[r]) or (dp[l + 1][r - 1] and s[l] == s[r]):
                    dp[l][r] = True
                    res += 1


        return res

