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


        #  ----- Deep Dive -----

        # Why binary search on the ANSWER (speed), not an array -> 

                # Normally binary search runs over an ARRAY (indices). Here, there's no sorted array to
                # search — instead, we binary-search over the RANGE OF POSSIBLE ANSWERS: the eating
                # speed k.

                #     the speed must be between 1 (slowest: 1 banana/hour) and max(piles) (fastest
                #     that's ever useful — eating faster than the biggest pile doesn't help, since you
                #     finish any pile in one hour at that speed).

                #     so the answer k lives in [1, max(piles)]. We binary-search THIS range.

                # Why can we binary-search speeds? Because the relationship is MONOTONIC (Tricky Part 2):
                #     faster speed → fewer hours needed. So "can Koko finish in ≤ h hours?" is a
                #     monotonic yes/no over speed — which is exactly what binary search needs.

                # The reframe: instead of "find the value in the array," it's "find the smallest speed k
                # in [1, max] for which the feasibility check passes." The search space is the ANSWER
                # RANGE, and we test each candidate speed with a feasibility function.

                #     this is "binary search on the answer" — applicable whenever the answer lies in a
                #     known range AND a monotonic feasibility check exists.

        

        # Why the feasibility check is monotonic (what makes binary search valid) -> 

                # Binary search requires a MONOTONIC condition: as you move through the search space,
                # the yes/no answer flips exactly once (all "no"s then all "yes"s, or vice versa).

                # Here, the condition is "can Koko finish in ≤ h hours at speed k?" As k INCREASES:
                #     - higher speed → fewer hours needed (you eat more per hour) → more likely to
                #     finish in time.
                #     - so there's a THRESHOLD speed: below it, too slow (hours > h, "no"); at or above
                #     it, fast enough (hours ≤ h, "yes").

                #     speed:   1    2    3    4    5    6 ...
                #     feasible? no   no   no   yes  yes  yes ...  (monotonic: flips once at the threshold)

                # We're looking for that THRESHOLD — the smallest k where "yes" begins. Binary search
                # finds it in O(log(range)):
                #     - if speed is feasible (hours ≤ h) → the answer is ≤ this speed → search slower
                #     (r = speed - 1), but remember this speed (res = speed).
                #     - if infeasible (hours > h) → need faster → search faster (l = speed + 1).

                # Without monotonicity, binary search would be invalid (you couldn't discard half). The
                # "faster always means fewer hours" guarantee is what makes it work.



        # Why math.ceil(p / speed) — the per-pile hours (and the "wasted leftover" rule) ->

                # At speed k, how many hours to eat a pile of p bananas? The key rule: Koko eats k per
                # hour, but FINISHES one pile before moving to the next — so leftovers in the final hour
                # of a pile are WASTED (she doesn't start the next pile mid-hour).

                #     this means each pile takes CEILING(p / k) hours:
                #     - p / k is the exact (fractional) hours.
                #     - ceil rounds UP because a partial hour still counts as a full hour (the leftover
                #     time is wasted, not carried over).

                #     e.g. pile of 7, speed 3: 7/3 = 2.33 → ceil = 3 hours.
                #     (hour 1: eat 3, hour 2: eat 3, hour 3: eat the last 1 — that 3rd hour is only
                #     partially used, but still a full hour. 3 hours total.)

                #     if we used p // k (floor) or p / k (exact), we'd UNDERCOUNT the hours → wrongly
                #     think a too-slow speed is feasible. The ceiling captures the "wasted leftover hour"
                #     rule.

                # Total hours = sum of ceil(p/k) over all piles. We compare this to h.

                #     (ceil(p / speed) can also be written as (p + speed - 1) // speed to avoid float —
                #     a common integer trick, same result.)



        # Why track minRate and search slower on success (finding the MINIMUM) -> 

                # We want the MINIMUM feasible speed. When we find a speed that works (hours ≤ h), it's
                # a valid answer — but maybe a SLOWER (smaller) speed also works. So we:
                #     1. RECORD it (res = speed) — it's the best answer so far.
                #     2. Keep searching SLOWER (r = speed - 1) — looking for an even smaller feasible
                #     speed.

                # If a slower speed also works, res gets updated to that smaller value. If not (slower
                # speeds are all too slow), res keeps the last feasible value we found — the minimum.

                #     this "record-and-keep-searching-for-smaller" is how you find the minimum value
                #     satisfying a condition via binary search. You don't stop at the first feasible
                #     one; you push toward the boundary.

                # When infeasible (hours > h), the speed is too slow → the answer is strictly faster →
                # l = speed + 1 (no recording, since this speed doesn't work).

                # At the end, res holds the smallest speed that passed the feasibility check = the
                # minimum eating speed. (Initializing res = max(piles) ensures a valid fallback, though
                # the search always finds a feasible speed since max(piles) always works.)



        # Why r = max(piles) — not sum(piles) -> It's a valid upper bound (correctness is fine), but it's needlessly large — you'd waste iterations searching speeds that behave identically. max(piles) is the tightest correct bound. Choosing tight bounds is a real skill in answer-space search. A loose bound still works but signals you haven't reasoned about the problem's structure.

        # Why l = 1 and not 0  -> k = 0 → ceil(p / 0) → ZeroDivisionError. And logically: eating 0 bananas per hour never finishes.

        # Why res = k before r = k - 1 -> Minimization search:  found a VALID answer? → it might not be the SMALLEST. Save it, then keep hunting left.

     






        

