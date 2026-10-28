class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom-up tabulation (fill a table)

        if n <= 2: 
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            # build up from smaller
            dp[i] = dp[i-1] + dp[i-2] 

        return dp[n]

        # Tabulation builds the answers iteratively from the smallest: dp[i] = dp[i-1] + dp[i-2], filling the array up to dp[n]. Same O(n) time, O(n) space. The space-optimized version just notices you only need the last two entries and drops the array. Knowing all four forms — and being able to walk from naive → memo → tabulate → optimize — is the core DP skill this section builds.