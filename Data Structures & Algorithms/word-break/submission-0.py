"""
Sol:
Brute Force Intuition:
At any i we try a word, if it works we check if the rest of the string
can be solved with wordDict as well

State:
The subproblem with bruteforce is rest of string is solvable.
dp[i] indicates s[i:] is solvable

Recurrence: 
(Note: expres dp state in terms of subproblem)
dp[i] = True if a word in wordDict matches from dp[i] AND dp[i + len of word]
is True.

Base case:
dp[len(s)] = True because we need one more in case empty string

Iteration Order:
Iterate from right to left as dp[i] depends on future states

Final Answer:
dp[0]
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            for word in wordDict:
                if s[i : i + len(word)] == word and dp[i + len(word)]:
                    dp[i] = True
        
        return dp[0]        

        