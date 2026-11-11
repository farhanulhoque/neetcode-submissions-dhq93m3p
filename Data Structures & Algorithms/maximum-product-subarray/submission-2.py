class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Track max & min (Kadane-style)
        
        # This is to store the best product found overall; start with the first element (a single element is a valid subarray)
        result = nums[0]
        # This is to store the maximum product of a subarray ending at the current position; start at nums[0]
        curMin = nums[0]
        # This is to store the minimum (most negative) product ending at the current position; start at nums[0]
        curMax = nums[0]

        # Process each element from index 1 onward
        for i in range(1, len(nums)):
            # The current number
            num = nums[i]
            # The three candidates for extending: the number alone (start fresh), number × previous max, number × previous min
            candidates = (num, num * curMax, num * curMin)

            # New curMax = the largest of the three (best product ending here)
            curMax = max(candidates)
            # New curMin = the smallest of the three (most negative product ending here)
            curMin = min(candidates)

            # Update the global best with the new curMax
            result = max(result, curMax)
        
        # Return the largest product found
        return result


        # TC: O(n) -> one pass over the array → O(n) iterations. Each iteration does O(1) work (three multiplications, a max, a min). O(n) overall.
        # SC: O(1) -> only three variables (res, curMax, curMin) regardless of n. No array, no recursion. O(1) overall.


        # Solution Description: 


        # ----- Deep Dive -----

        # Why we track the MIN as well as the max -> With SUMS (Kadane's / Maximum Subarray), you only track the max — adding a negative always makes things smaller, so the min is useless for maximizing.

                # With PRODUCTS, negatives FLIP signs:
                #     a large NEGATIVE product × a negative number → a large POSITIVE product.

                # So the smallest (most negative) product so far is a CANDIDATE to become the largest,
                # if the next number is negative. We MUST track it.

                #     nums = [-2, -3]:
                #         at -2: curMax = -2, curMin = -2.
                #         at -3: num × curMin = -3 × -2 = 6 → the MIN flipped into the MAX!
                #         if we'd only tracked curMax (-2 × -3 = 6, actually same here)... but consider
                #         nums = [2, -3, -4]:
                #             at 2: curMax=2, curMin=2.
                #             at -3: candidates (-3, -3×2=-6, -3×2=-6) → curMax=-3, curMin=-6.
                #             at -4: candidates (-4, -4×-3=12, -4×-6=24) → curMax=24!
                #             the 24 came from num × curMin (-4 × -6) — the MIN flipped into the best.
                #             without tracking curMin, we'd have missed it. 

                # So the min isn't "the worst answer" — it's a FUTURE max waiting for a negative to
                # flip it. That's why we track both.



        # Why three candidates — num, num × curMax, num × curMin -> At each number, the best (or worst) product ending HERE is one of three things: 

                # 1. num alone — START A FRESH subarray at this element. This handles the case
                # where the previous products are bad (e.g. a zero reset everything, or
                # extending would only hurt).

                # 2. num × curMax — EXTEND the previous max product. If num is positive, this
                # grows a positive max; if num is negative, this makes a negative (a min
                # candidate).

                # 3. num × curMin — EXTEND the previous min product. If num is negative, this
                # can flip a very-negative min into a large positive (the key case).


                # The new curMax is the LARGEST of these three; the new curMin is the SMALLEST. We
                # consider all three because we don't know num's sign in advance — any of the three
                # could be the new extreme.

                # why "num alone"? because sometimes RESTARTING beats extending — e.g. after a 0
                # (num×curMax and num×curMin would be 0), or when the running products are worse
                # than the number itself.
        


        # Why num alone handles zeros (the reset) -> 

                # Zeros are a subtle case. When num = 0:
                #     num × curMax = 0, num × curMin = 0, and num alone = 0.
                #     → curMax and curMin both become 0.

                # Then the NEXT number effectively STARTS FRESH:
                #     next candidates = (next, next×0, next×0) = (next, 0, 0) → curMax = max of those
                #     = next (if positive). So the zero "reset" the running products, and the subarray
                #     restarts after it.

                # The "num alone" candidate is what allows this restart — without it, a 0 could trap
                # the products at 0 forever. With it, the subarray naturally breaks at zeros and begins
                # again.

                #     nums = [-2, 0, -3, -4]:
                #         the 0 resets curMax/curMin to 0. Then -3, -4 start a fresh subarray →
                #         -3×-4 = 12. The answer is 12, from the subarray AFTER the zero. 



        # Why compute candidates BEFORE updating curMax/curMin -> Both new curMax and new curMin depend on the OLD (previous) curMax and curMin. If we updated curMax first, then computed curMin using the NEW curMax, we'd use the wrong value. 

                # e.g. if we did:
                #     curMax = max(num, num*curMax, num*curMin)   # curMax updated
                #     curMin = min(num, num*curMax, num*curMin)   # BUG: uses the NEW curMax!
                # the curMin computation would use the just-updated curMax, not the original →
                # wrong.

                # The fix: compute all three candidates FIRST (using the old values), store them, THEN
                # derive both curMax and curMin from that frozen snapshot. This ensures both updates use
                # the same (previous) state.

                # Storing candidates in a tuple is a clean way to freeze the snapshot — compute
                # once, use for both max and min.



        # ----- Edge Cases -----

        # Single element -> oop doesn’t run; returns res = nums[0] (a single element is a valid subarray).

        # Contains a zero -> The zero resets curMax/curMin to 0; subarrays before and after are considered separately.

        # All negatives (even count) -> Multiplying all gives a positive → the full product is the max (the min-tracking catches the sign flips).

        # All negatives (odd count) -> The full product is negative; the best is a subarray excluding one negative — min-tracking finds it.

        # Single negative -> Returns that negative (the only subarray).

        # Negative + zero mix -> Zeros reset; the best product comes from a run between zeros.







