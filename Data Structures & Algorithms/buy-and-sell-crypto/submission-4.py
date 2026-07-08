class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 0
        maxProfit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right 
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            right += 1
        
        return maxProfit