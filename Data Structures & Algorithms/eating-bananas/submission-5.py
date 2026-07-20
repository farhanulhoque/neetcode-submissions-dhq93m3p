class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Search space is speeds, not indices: 1 (slowest) to max(piles) (fastest that matters)
        left, right = 1, max(piles)
        minRate = right

        while left <= right:
            k = left + (right - left) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                minRate = k
                right = k - 1
            else:
                left = k + 1
        
        return minRate

        # TC: O(n * log(max(piles))) -> Binary search runs log₂(max(piles)) iterations. Each iteration does an O(n) feasibility scan over all piles. Note the multiplication — unlike plain binary search, each step isn't O(1)
        # SC: O(1) -> Just l, r, k, res, hours — no extra structures

        # The shape of the complexity -> Plain binary search is O(log n) because checking mid costs O(1). Here, checking mid costs O(n) — so it's O(n log m), where n and m are different quantities: n = number of piles, m = size of the largest pile.

        # Solution Description: The answer k isn't in piles — it's a speed we choose. But the candidate speeds form a sorted range: 1 (slowest useful) to max(piles) (fastest useful — eating faster than the biggest pile can't help, since you can only eat from one pile per hour). The key property: if speed k works, every speed above k also works. So the answers look like [✗, ✗, ✗, ✓, ✓, ✓] — a monotonic step function. Binary search over that range: compute the hours needed at mid; if it fits in h, record mid as a candidate and search left for something smaller; if not, search right for something faster.