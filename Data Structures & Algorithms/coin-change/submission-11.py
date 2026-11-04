class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(a):
            if a == 0: return 0
            if a < 0: return float('inf')       # overshot — invalid
            if a in memo: return memo[a]
            res = min(dfs(a - c) + 1 for c in coins)   # try each coin
            memo[a] = res
            return res
        result = dfs(amount)
        return result if result != float('inf') else -1