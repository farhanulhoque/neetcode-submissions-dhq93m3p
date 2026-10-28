class Solution:
    def climbStairs(self, n: int) -> int:
        # Top-down memoization (recursion + cache)
        
        memo = {}
        def dfs(i):
            if i <= 2: 
                return i
            # already computed → return cached
            if i in memo: 
                return memo[i]        
            # compute once, store
            memo[i] = dfs(i-1) + dfs(i-2)       
            return memo[i]
        return dfs(n)