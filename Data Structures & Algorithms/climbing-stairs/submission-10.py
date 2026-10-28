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

        # Memoization adds a cache to the naive recursion: before computing dfs(i), check if it’s cached; store each result. Each subproblem is computed once → O(n). This is the easiest DP form to derive (just add a cache to the obvious recursion), and a great way to start a DP problem before optimizing.