class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left and right bound the search
        left, right = 0, len(nums) - 1

        # l < r (not <=) — we stop when the range narrows to one element, which is the min
        while left < right:
            # Find Overflow-safe midpoint
            mid = left + (right - left) // 2

            # the right half is "broken" → the minimum must be there. Discard the left half and mid — the min is strictly right of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise the right half [mid..r] is properly sorted. The min is at mid or to its left → move r to mid (keep mid as a candidate)
            else:
                right = mid
        # left and right have converged on the minimum
        return nums[left]

        # TC: O(logn) -> Each iteration discards half the range with O(1) work — a single comparison against nums[r]. Classic logarithmic halving
        # SC: O(1) -> Only l, r, mid — no extra structures

        # Solution Description: A rotated sorted array has one "break point" where a big number is immediately followed by the smallest — that smallest is the minimum. The insight enabling O(log n): comparing nums[mid] to nums[r] tells us which side the break is on. If nums[mid] > nums[r], the right half is out of order — the break (and thus the minimum) lies strictly to the right of mid, so move l = mid + 1. Otherwise nums[mid] <= nums[r] means the right half is properly sorted, so the minimum is at mid or to its left — move r = mid. We keep the current mid as a candidate (don't skip it with mid - 1) because mid itself could be the minimum.
        

        # ----- Deep Dive -----

        # Why compare to nums[r] and NOT nums[l] -> 

                # A rotated sorted array has two sorted "runs," with the minimum at the break:
                #     [3, 4, 5, 1, 2]  → run [3,4,5] then run [1,2]; min (1) is where it drops.

                # We compare nums[mid] to nums[r] (the RIGHT boundary) to figure out which side the
                # minimum is on:

                #     nums[mid] > nums[r]:
                #         mid is in the LEFT (higher) run, and the drop-to-minimum is somewhere to the
                #         RIGHT of mid. Why? If mid were in the same run as r (or r itself), mid would
                #         be ≤ r (sorted). mid being GREATER than r means a "drop" happens between mid
                #         and r → the minimum is strictly after mid.
                #         → search the right half: l = mid + 1.

                #     nums[mid] <= nums[r]:
                #         mid and r are in the SAME sorted run (mid ≤ r, no drop between them). So the
                #         minimum is at mid or to the LEFT of mid (the drop, if any, is before mid).
                #         → search including mid: r = mid.

                # Why nums[r] and NOT nums[l]? Comparing to nums[l] is AMBIGUOUS:
                #     if nums[mid] > nums[l], the min could be left OR right (depends on where the
                #     rotation is) — you can't decide cleanly. But comparing to nums[r] is UNAMBIGUOUS:
                #     nums[mid] > nums[r] ALWAYS means the min is to the right, because the right portion
                #     is the lower run. The right boundary gives a clean yes/no.

                #     (intuition: nums[r] is always in the "lower" run (or the whole array if unrotated),
                #     so comparing to it reliably tells you which side of the break mid is on.)



        # Rule of thumb for rotated arrays -> compare to the boundary that the minimum has a fixed relationship with. The min is always ≤ nums[r], so nums[r] is the reliable reference. Its relationship to nums[l] flips depending on rotation.



        # Why while l < r and not l <= r -> 

                # Unlike classic binary search (which looks for a target and uses l <= r, returning
                # when found or -1), here we're CONVERGING on the single minimum element. We shrink
                # [l, r] until l and r meet at one index — that index IS the minimum.

                #     while l < r: keep going while the range has MORE than one element.
                #     when l == r: the range has collapsed to ONE element → that's the answer → exit.

                # Why not l <= r? With l <= r and r = mid (not mid-1), you could get an infinite loop:
                #     if l == r, the loop body runs, mid == l == r, and r = mid keeps r == l forever →
                #     never terminates. 

                # Using l < r guarantees termination: the range strictly shrinks each iteration (either
                # l = mid+1 moves l up, or r = mid moves r down since mid < r when l < r), and we stop
                # the instant l meets r.

                #     this is the "find the boundary / converge to one" binary-search variant, different
                #     from the "find exact target" variant. The condition and return differ accordingly.
        


        # Why l = mid + 1 but r = mid (asymmetric updates) -> 

                # The two branches update differently, and the asymmetry encodes "can mid be the answer?"

                #     l = mid + 1 (exclude mid): when nums[mid] > nums[r], mid is in the higher run and
                #     is DEFINITELY NOT the minimum (something smaller is to the right). So we safely
                #     skip mid → l = mid + 1.

                #     r = mid (include mid): when nums[mid] <= nums[r], mid COULD BE the minimum itself
                #     (it's the smallest in its run, and the min is at mid or to the left). So we must
                #     KEEP mid in the range → r = mid (not mid - 1).

                # If we wrongly did r = mid - 1 in the second branch, we might SKIP OVER the minimum:
                #     e.g. if mid IS the minimum, r = mid - 1 would exclude it → we'd lose the answer. 

                # The rule: exclude an index only when you're CERTAIN it's not the answer. Here, the
                # left branch is certain (mid > nums[r] → not min → exclude), but the right branch is
                # not (mid might be the min → include). Hence mid+1 vs mid.

                #     (this pairs with the while l < r condition: r = mid keeps shrinking the range
                #     since mid < r whenever l < r, so no infinite loop, and mid is never wrongly
                #     skipped.)


        # Why this handles the already-sorted (not rotated) case -> 

                # If the array isn't rotated at all, it's just sorted, and the minimum is the FIRST
                # element. Does the logic handle this?

                #     [1,2,3,4,5]: l=0, r=4.
                #     mid=2 (val 3): nums[2]=3 > nums[4]=5? no (3 <= 5) → r = mid = 2.
                #     mid=1 (val 2): nums[1]=2 > nums[2]=3? no → r = 1.
                #     mid=0 (val 1): nums[0]=1 > nums[1]=2? no → r = 0.
                #     l == r == 0 → return nums[0] = 1. ✓

                # Because nums[mid] <= nums[r] is ALWAYS true in a fully sorted array (every element ≤
                # the last), the "else" branch (r = mid) always fires, driving r down to index 0 — the
                # minimum. The algorithm naturally converges to the first element.

                # No special-casing needed: the "compare to nums[r]" logic treats "not rotated" as a
                # rotation by 0, and the minimum (first element) falls out correctly.


        # Convergence binary search (find a boundary) uses l < r and returns nums[l]. Target binary search (find a value) uses l <= r and returns from inside.


        # Because at least one half is always clean, comparing mid to r reliably reveals which side the break (minimum) is on.


        # A rotated sorted array is two sorted runs. Pick any mid. The split [l..mid] and [mid..r]: the break point lies in exactly ONE of these halves → the OTHER half is a single unbroken sorted run







        