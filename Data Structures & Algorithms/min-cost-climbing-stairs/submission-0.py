class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #DP[i] is OPT[i], here DP[i] is the min cost to reach ith floor
        dp = [0] * (len(cost) + 1) # past last index in cost
        
        #base cases, 0 since you can choose to start at 0 or 1st floor
        dp[0] = 0
        dp[1] = 0

        #recurrence relation -> step to i + 1 or step to i + 2
        # DP[i] = min(cost[i - 1] + DP[i - 1], cost[i - 2] + DP[i -2])
        for i in range(2, len(cost) + 1):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i -2])


        return dp[len(cost)]