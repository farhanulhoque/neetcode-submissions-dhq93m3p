class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Bottom-up tabulation (the array version

        n = len(cost)
        # dp[i] = min cost to reach floor i. dp[0] = dp[1] = 0 (free to start)
        dp = [0] * (n + 1)              
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]

        # Tabulation uses a full dp array where dp[i] = min cost to reach floor i, filling it from the base cases up to dp[n] (the top). Same O(n) time, but O(n) space. It’s clearer to read (each dp[i] is explicit) and a good intermediate form before the space optimization — which just notices you only ever need dp[i-1] and dp[i-2], so two variables suffice. Lead with the optimized version in an interview, but tabulation is fine and arguably more readable.