class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        maxProfit = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
        
        return maxProfit