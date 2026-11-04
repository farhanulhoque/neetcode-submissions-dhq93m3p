class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top-down memoization

        memo = {}
        def dfs(a):
            if a == 0:
                return 0
            # overshot — invalid
            if a < 0:
                return float("inf")
            if a in memo:
                return memo[a]
                
            # try each coin
            result = min(dfs(a - c) + 1 for c in coins)
            memo[a] = result
            
            return result
        
        result = dfs(amount)

        return result if result != float("inf") else -1


        # Memoization mirrors the recurrence directly: dfs(a) = fewest coins for amount a, trying each coin (dfs(a - c) + 1) and taking the min, with a < 0 meaning “overshot/invalid.” The cache makes each amount computed once → O(amount · C)




