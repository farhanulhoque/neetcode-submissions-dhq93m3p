class Solution:
    def rob(self, nums: List[int]) -> int:
        # Space-optimized

        # prev2 = max money robbable up to two houses back (before the previous house); starts at 0
        prev2 = 0
        # prev1 = max money robbable up to the previous house; starts at 0
        prev1 = 0
        
        # Process each house’s money "num" in order
        for num in nums:
            # The decision: skip this house (prev1, keep the previous best) or rob it (prev2 + num, this house’s money plus the best up to two houses back) — take the larger
            curr = max(prev1, prev2 + num)
            # Slide the window: prev2 becomes what prev1 was
            prev2 = prev1
            # prev1 becomes the newly computed curr
            prev1 = curr
        
        # After processing all houses, prev1 holds the maximum robbable amount
        return prev1


        # TC: O(n) -> the loop processes each house once → O(n) iterations. Each iteration does O(1) work (a max, an add, two assignments). O(n) overall.
        # SC: O(1) -> only three variables (prev2, prev1, curr) regardless of n. No array, no recursion. O(1) — the space-optimized form.

        # Full-array bottom-up: O(n) space. Naive recursion: O(2ⁿ) time. This optimized version: O(n) time, O(1) space.


        # Solution Description: At each house, you face a decision: rob it or skip it. If you rob house i, you get nums[i] but can’t rob house i-1 (adjacent) — so you add nums[i] to the best you could do up to house i-2. If you skip house i, your best is whatever you had up to house i-1. You take whichever is larger: dp[i] = max(dp[i-1], dp[i-2] + nums[i]). dp[i] = the maximum money robbable considering houses 0..i. Base cases anchor the first one or two houses. Since dp[i] only needs the previous two values, we keep two variables → O(1) space. I’ll lead with the space-optimized version.


        # ----- Deep Dive -----

        # The include/exclude decision — the heart of the recurrence -> At each house, you DECIDE: rob it or skip it. The recurrence captures both choices and takes the better:  

                    # SKIP house i:  you don't take its money → your best is unchanged from the
                    #             previous house → dp[i-1] (prev1).

                    # ROB house i:   you take nums[i], but then you CAN'T have robbed house i-1
                    #             (adjacent → would alert police). So you add nums[i] to the
                    #             best you could do up to house i-2 (NOT i-1) → dp[i-2] + nums[i]
                    #             (prev2 + num).

                    # dp[i] = max(skip, rob) = max(prev1, prev2 + num).

                    # The KEY subtlety: robbing house i means adding to dp[i-2], NOT dp[i-1] — because
                    # house i-1 is adjacent and off-limits if you rob i. This "+dp[i-2]" is what
                    # enforces the no-adjacent constraint.

                    # Why max (not sum or min)? We're MAXIMIZING money, and at each house we pick the BETTER of two mutually-exclusive choices (rob or skip). Max over the choices.
        


        # Why rob adds to dp[i-2], not dp[i-1] (the constraint mechanism) -> Robbing house i adds to dp[i-2] (two back), not dp[i-1], because robbing i forbids robbing the adjacent i-1 — so the best prior total must come from before i-1. This +dp[i-2] is the no-adjacent constraint, made concrete in the recurrence. Adding to dp[i-1] would allow two adjacent robberies → wrong


        # Why base cases of 0 work (and the clean loop-over-nums form) -> Both start at 0, representing "max money robbable from NO houses yet = 0."

                # Walking through the first iterations:
                #     house 0 (num = nums[0]):
                #         curr = max(prev1=0, prev2=0 + nums[0]) = max(0, nums[0]) = nums[0].
                #         → with one house, you rob it → nums[0]. ✅
                #     house 1 (num = nums[1]):
                #         curr = max(prev1=nums[0], prev2=0 + nums[1]) = max(nums[0], nums[1]).
                #         → with two adjacent houses, rob the richer one. ✅

                # Starting both at 0 cleanly handles the base cases WITHOUT special-casing the
                # first two houses. The loop-over-nums form (iterating values directly) is elegant:
                # prev2=0 means "two houses before house 0 = nothing", prev1=0 means "before house
                # 0 = nothing", and the recurrence naturally produces the right early values.
        


        # Why the sliding window works (the space optimization) -> Same space optimization as the previous DP problems: dp[i] only needs dp[i-1] (prev1) and dp[i-2] (prev2). We never look further back.

                # So instead of a full dp array, we keep two variables and slide them forward each house:
                #     curr = max(prev1, prev2 + num)   ← compute dp[i]
                #     prev2 = prev1                     ← dp[i-2] becomes dp[i-1] for next iteration
                #     prev1 = curr                      ← dp[i-1] becomes dp[i]

                #     → O(1) space. The "window" of the last two best-totals slides along the houses.

                # The order matters: save prev1 into prev2 BEFORE overwriting prev1 with curr,
                # or you'd lose the old prev1 value needed for the slide.



        # ----- Edge Cases -----

        # Empty array (nums=[]) -> The loop never runs; returns prev1 = 0. No houses → rob nothing → 0.

        # One house -> Loop runs once: max(0, 0 + nums[0]) = nums[0] → rob the only house.






