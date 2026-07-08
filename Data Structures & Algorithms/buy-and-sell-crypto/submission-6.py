class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left starts at day 0 — our initial candidate buy day
        left = 0
        # This is to track best profit found so far
        maxProfit = 0

        # right is the sell day — start at day 1 since we can't sell on the buy day
        for right in range(1, len(prices)):
            # If the price at right is lower than our buy price, this is a better day to buy — shift left pointer
            if prices[right] < prices[left]:
                left = right
            # Otherwise, prices[right] is higher — a potential profit
            else:
                # Compute profit: sell price - buy price
                profit = prices[right] - prices[left]
                # Update running maximum if this profit beats our best
                maxProfit = max(maxProfit, profit)
        
        return maxProfit

        # TC: O(n) -> Single pass — right moves through the array once, left only ever jumps forward
        # SC: O(1) -> Just two pointers and a running maximum — no extra structures

        # Solution Description: Keep a l pointer on the best day to buy (lowest price so far) and slide a r pointer forward as the sell day. For each sell day, compute the profit if we had bought at l. If the price at r is lower than our buy price, it's a better future buy point — move l to r. Otherwise, compute the profit and update our running maximum. We never sell before we buy because r always stays ahead of l.
        