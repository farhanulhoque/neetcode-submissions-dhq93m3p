class Solution:
    def rob(self, nums: List[int]) -> int:
        # Bottom-up tabulation (the array version)

        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            # skip vs rob
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])   
        return dp[n-1]

        # Tabulation uses a dp array where dp[i] = max robbable from houses 0..i, with explicit base cases dp[0]=nums[0] and dp[1]=max(nums[0],nums[1]). Same O(n) time, O(n) space. The space-optimized version collapses this to two variables since dp[i] only needs dp[i-1] and dp[i-2]. Tabulation is clearer to read (the base cases are explicit); the loop-over-nums optimized form is more elegant. Both are fine in an interview.