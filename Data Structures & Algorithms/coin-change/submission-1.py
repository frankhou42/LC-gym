"""
dp[i] holds fewest number of coins needed to make up integer i
At each integer for each coin we can choose minimum of dp[i-coin] + 1
and dp[i] (as dp[i] holds min across all coins)

smallest state is amount = 0 so we need dp 0 which means we have amount + 1
since 0-based indexiong
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)

        #base case 
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1



        