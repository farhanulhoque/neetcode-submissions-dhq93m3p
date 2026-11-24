class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top-down memoization

        memo = {}
        def dfs(amt):
            if amt == 0:
                return 0
            # overshot — invalid
            if amt < 0:
                return float("inf")
            if amt in memo:
                return memo[amt]
                
            # try each coin
            result = float("inf")
            for c in coins:
                diff = amt - c
                result = min(result, dfs(diff) + 1)

            memo[amt] = result
            
            return result
        
        result = dfs(amount)

        return result if result != float("inf") else -1


        # Memoization mirrors the recurrence directly: dfs(a) = fewest coins for amount a, trying each coin (dfs(a - c) + 1) and taking the min, with a < 0 meaning “overshot/invalid.” The cache makes each amount computed once → O(amount · C)




