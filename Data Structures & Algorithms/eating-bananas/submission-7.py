class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Search space is speeds, not indices: 1 (slowest) to max(piles) (fastest that matters)
        left, right = 1, max(piles)
        # This is to track the best valid answer found. Initialize to max(piles) — always guaranteed to work
        minRate = right

        # Standard inclusive-bound binary search loop
        while left <= right:
            # k is the candidate speed we're testing this round
            k = left + (right - left) // 2

            # Accumulate total hours needed at this speed. Check every pile. Hours for this pile = ceil(p / k) — a leftover partial hour still costs a whole hour
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            # If this speed works — we finish within the deadline. Record it as a valid answer. But maybe a slower speed also works → search left for something smaller.
            if hours <= h:
                minRate = k
                right = k - 1
            # If too slow — we ran out of hours → search right for a faster speed
            else:
                left = k + 1
        
        # Return the smallest speed that worked
        return minRate

        # TC: O(n * log(max(piles))) -> Binary search runs log₂(max(piles)) iterations. Each iteration does an O(n) feasibility scan over all piles. Note the multiplication — unlike plain binary search, each step isn't O(1)
        # SC: O(1) -> Just l, r, k, res, hours — no extra structures

        # The shape of the complexity -> Plain binary search is O(log n) because checking mid costs O(1). Here, checking mid costs O(n) — so it's O(n log m), where n and m are different quantities: n = number of piles, m = size of the largest pile.

        # Solution Description: The answer k isn't in piles — it's a speed we choose. But the candidate speeds form a sorted range: 1 (slowest useful) to max(piles) (fastest useful — eating faster than the biggest pile can't help, since you can only eat from one pile per hour). The key property: if speed k works, every speed above k also works. So the answers look like [✗, ✗, ✗, ✓, ✓, ✓] — a monotonic step function. Binary search over that range: compute the hours needed at mid; if it fits in h, record mid as a candidate and search left for something smaller; if not, search right for something faster.

        # We're binary searching a space that doesn't exist in the input. In every previous binary search, l and r were array indices. Here they're candidate answers. Binary search isn't "find a value in a list." It's "find a boundary in a monotonic space." The list is just the most common such space.
        # Why r = max(piles) — not sum(piles) -> It's a valid upper bound (correctness is fine), but it's needlessly large — you'd waste iterations searching speeds that behave identically. max(piles) is the tightest correct bound. Choosing tight bounds is a real skill in answer-space search. A loose bound still works but signals you haven't reasoned about the problem's structure.
        # Why l = 1 and not 0  -> k = 0 → ceil(p / 0) → ZeroDivisionError. And logically: eating 0 bananas per hour never finishes.
        # Why res = k before r = k - 1 -> Minimization search:  found a VALID answer? → it might not be the SMALLEST. Save it, then keep hunting left.
        # Ceiling division — and why // is wrong -> The problem's rule: leftover bananas still cost a full hour, and you can't move to another pile with the leftover time. Floor division would undercount hours, making slow speeds look feasible → wrong (too small) answer.

