class Solution:
    def rob(self, nums: List[int]) -> int:
        # Two linear runs (reduction)

        # If there’s only one house, rob it (can’t exclude either endpoint when there’s only one — special case)
        if len(nums) == 1:
            return nums[0]

        # Helper: the linear House Robber on a given list of houses   
        def robLinear(houses):
            # Base cases: max robbable from no houses = 0 (both sliding variables)
            prev2 = 0
            prev1 = 0

            # Process each house’s money
            for num in houses:
                # The rob-or-skip decision: skip (prev1) or rob (prev2 + num) — take the larger
                curr = max(prev1, prev2 + num)
                # Slide the window: prev2 becomes the old prev1
                prev2 = prev1 
                # prev1 becomes the new curr
                prev1 = curr
            
            # Return the max robbable for this linear range
            return prev1
        
        # Case A: exclude house 0 → run linear House Robber on houses 1..n-1 (nums[1:]). Case B: exclude house n-1 → run linear House Robber on houses 0..n-2 (nums[:-1]); return the max of the two cases.
        return max(robLinear(nums[1:]), robLinear(nums[:-1]))


        # TC: O(n) -> robLinear runs in O(n) (one pass over its range). We call it TWICE (on sub-ranges of size ~n each) → 2 · O(n) = O(n). The n=1 check is O(1). O(n) overall — the constant factor of 2 doesn't change the big-O.
        # SC: O(n) [or O(1) with index-based ranges] -> robLinear itself uses O(1) (two sliding variables). BUT nums[1:] and nums[:-1] create SLICE COPIES of size ~n each → O(n) space. To get O(1) space, pass START/END INDICES to robLinear instead of slicing (iterate nums[start:end] via indices, no copy). O(n) as written (due to slicing); O(1) with the index-based version.


        # Solution Description: The only difference from House Robber is that house 0 and house n-1 are now adjacent (the circle), so you can’t rob both. The elegant insight: this means in any valid robbery, at least one of the two endpoints is NOT robbed. That gives two cases: Case A: don’t rob house 0 → rob freely among houses 1..n-1 (a linear row), Case B: don’t rob house n-1 → rob freely among houses 0..n-2 (a linear row). Each case is just the linear House Robber on a sub-range (which has no circular constraint, since we’ve dropped one endpoint). The answer is the max of the two cases. We reuse the exact House Robber helper twice. One edge case: a single house (no range to exclude) is handled directly.


        # ----- Deep Dive -----

        # The core insight — circular reduces to two linear runs -> The circle adds ONE new constraint: house 0 and house n-1 are adjacent → you can't rob BOTH. Key observation: in ANY valid robbery, at least one of {house 0, house n-1} is NOT robbed (you can't take both). So every valid solution falls into one of two cases:

                # CASE A: house 0 is NOT robbed → the remaining houses 1..n-1 form a LINE (no
                #         wrap-around, since house 0 is out) → plain linear House Robber.

                # CASE B: house n-1 is NOT robbed → houses 0..n-2 form a LINE → linear House
                #         Robber.

                # The true answer is the BEST of these two cases: max(caseA, caseB). Why these two cases COVER everything: any valid robbery skips at least one endpoint. If it skips house 0, it's covered by Case A; if it skips house n-1, Case B. (A robbery skipping both is covered by either.) No valid solution is missed, and neither case can rob both endpoints (each excludes one), so the circular constraint is satisfied.

                # We DON'T invent a new circular DP. We REDUCE the circle to two instances of the LINEAR problem we already solved. Dropping one endpoint breaks the circle into a line.
        


        # Why excluding one endpoint breaks the circular constraint -> Excluding one endpoint eliminates the wrap-around adjacency — the circle’s only extra rule is “not both endpoints,” so removing either one leaves a pure line with no circular constraint. nums[1:] (drop house 0) and nums[:-1] (drop house n-1) are the two linear sub-ranges. All middle adjacencies are identical to the linear problem; only the endpoint pair is special, and dropping one defuses it.


        # Why the single-house case needs special handling -> With one house, nums[1:] = [] and nums[:-1] = [] — BOTH sub-ranges are EMPTY. robLinear([]) returns 0 (no houses to rob). So max(robLinear([]), robLinear([])) = max(0, 0) = 0 → WRONG. We should rob the single house → nums[0].

                # The issue: with one house, you can't "exclude an endpoint" and still have houses left — excluding either endpoint removes the only house. So the two-case reduction breaks down for n=1.

                # The fix: handle n=1 directly (return nums[0]) before the reduction.

                # n=2 is fine: nums[1:]=[nums[1]], nums[:-1]=[nums[0]] → max(nums[1], nums[0]), the richer of two adjacent houses. Only n=1 needs the special case.
        


        # Why we reuse the exact linear helper (no modification) -> robLinear is EXACTLY the House Robber I solution — unchanged. We don't modify the DP at all; we just CALL it on two different sub-ranges. This is the payoff of the reduction: the circular problem needs NO new DP logic. The linear solution, applied twice to the right sub-ranges, fully solves it. Reduction turns "solve a new, harder problem" into "call an existing solution twice and take the max."



        # ----- Edge Cases -----

        # Single house (n=1) -> The len(nums) == 1 guard returns nums[0] directly — the reduction would wrongly give 0.

        # Two houses (n=2) -> max(robLinear([nums[1]]), robLinear([nums[0]])) = max(nums[1], nums[0]) → the richer of the two adjacent houses.

        # Empty array (n=0)	-> Not typically given (n ≥ 1); if it were, you’d guard for it (both sub-ranges empty → 0).






