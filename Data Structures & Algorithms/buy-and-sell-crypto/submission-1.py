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

        # TC: O(n) -> Single pass — right moves through the array once, left only ever jumps forward
        # SC: O(1) -> Just two pointers and a running maximum — no extra structures

        # Solution Description: Keep a l pointer on the best day to buy (lowest price so far) and slide a r pointer forward as the sell day. For each sell day, compute the profit if we had bought at l. If the price at r is lower than our buy price, it's a better future buy point — move l to r. Otherwise, compute the profit and update our running maximum. We never sell before we buy because r always stays ahead of l.
        