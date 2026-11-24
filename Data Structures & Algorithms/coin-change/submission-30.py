class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dfs(a):
            if a == 0:
                return 0
            if a in memo:
                return memo[a]
            if a < 0:
                return float("inf")
            

            result = min(dfs(a - c) + 1 for c in coins)
            
            memo[a] = result

            return result
        
        result = dfs(amount)

        return result if result != float("inf") else -1