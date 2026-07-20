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
        
        # Why compare to nums[r] and NOT nums[l] -> Comparing nums[mid] against the right boundary gives a clean, unambiguous decision. Comparing against the left does not. nums[mid] > nums[r]: mid's value is BIGGER than the rightmost → impossible in a sorted stretch → the "break" is between mid and r → minimum is RIGHT of mid. nums[mid] <= nums[r]: mid to r is properly ascending → that stretch is sorted, no break there → minimum is at mid or LEFT of it. nums[l] can't distinguish "not rotated" from "rotated". nums[r] can — because the minimum is always <= nums[r], never > it.
        # Rule of thumb for rotated arrays -> compare to the boundary that the minimum has a fixed relationship with. The min is always ≤ nums[r], so nums[r] is the reliable reference. Its relationship to nums[l] flips depending on rotation.
        # Why while l < r and not l <= r -> If we used l <= r here: at l == r, mid == l == r the else branch does r = mid → r stays the same → l stays the same → INFINITE LOOP
        # Convergence binary search (find a boundary) uses l < r and returns nums[l]. Target binary search (find a value) uses l <= r and returns from inside.
        # Why r = mid and NOT r = mid - 1 -> In the else branch, nums[mid] <= nums[r], meaning: mid is in the sorted right stretch → mid COULD BE the minimum itself! If we did r = mid - 1, we'd discard mid — potentially throwing away the answer. nums[mid] > nums[r] proves mid is NOT the minimum (something smaller exists to its right). So excluding mid with +1 is safe — we KNOW mid isn't the answer.
        # Because at least one half is always clean, comparing mid to r reliably reveals which side the break (minimum) is on.
        # A rotated sorted array is two sorted runs. Pick any mid. The split [l..mid] and [mid..r]: the break point lies in exactly ONE of these halves → the OTHER half is a single unbroken sorted run