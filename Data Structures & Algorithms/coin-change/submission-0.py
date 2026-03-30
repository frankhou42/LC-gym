"""
dp[i] is the minimum amount of coins to make amount i
At each amount i dp[i] = minimum for all coin (dp[i - coin] + 1)

initiate the dp arr as all infinity so that we can find minimum

amount + 1 here because we consider empty state

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) #creates a list
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1