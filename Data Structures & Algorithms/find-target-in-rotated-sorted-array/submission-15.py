class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left and right bound the whole array
        left, right = 0, len(nums) - 1

        # Target-search style — <= so the single-element range is still checked
        while left <= right:
            # Find Overflow-safe midpoint
            mid = left + (right - left) // 2

            # Direct hit — return the index immediately
            if nums[mid] == target:
                return mid
            
            # if the left half [l..mid] is properly sorted
            if nums[left] <= nums[mid]:
                # Is the target within the left half's range [nums[l], nums[mid]). If Yes — search the left half. mid already checked on → exclusive
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # target must be in the right half
                else:
                    left = mid + 1
            # Otherwise the right half [mid..r] is properly sorted
            else:
                # Is the target within the right half's range (nums[mid], nums[r]]. If Yes — search the right half. mid already checked on → exclusive
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # target must be in the left half
                else:
                    right = mid - 1
        # Pointers crossed — target not present
        return -1

        # TC: O(logn) -> Each iteration halves the search space with O(1) comparisons. The extra branching decides direction, not count — still logarithmic
        # SC: O(1) -> Only l, r, mid — no extra structures

        # Solution Description: This fuses the sorted-half insight from Find Minimum with a target search. At each step, at least one half of the array is properly sorted. Determine which half is sorted by comparing nums[mid] to nums[l]. Then check whether the target lies within that sorted half's range — if yes, search there; if no, search the other half. The reasoning: we can only make a clean "is the target in this half?" decision on the sorted half, because its bounds are trustworthy (nums[l] to nums[mid], or nums[mid] to nums[r]). The broken half's bounds don't reliably bracket its contents, so we handle it by elimination — if the target isn't in the sorted half, it must be in the other.
        
        # Why identify the sorted half FIRST -> In a normal sorted array, nums[mid] < target instantly tells you to go right. In a rotated array, that logic breaks — a bigger mid value might sit to the left of the target due to the rotation. The fix: first figure out which half is sorted, because only a sorted half lets you reliably ask "does the target fall in this range?"
        # Why nums[l] <= nums[mid] detects the sorted-left half -> If the left half had the break in it, nums[l] would be a BIG value and somewhere before mid it would drop to a small value — making nums[mid] < nums[l]. So nums[l] <= nums[mid] GUARANTEES no break in [l..mid] → the left half is a clean ascending run.
        # Why <= and not < -> When l == mid (a two-element or one-element range), nums[l] == nums[mid] — that single element is trivially "sorted," so <= correctly classifies it as the left-sorted case.
        # The range checks — why the specific < vs <= placement -> nums[mid] was already tested for equality, so it's excluded from both range checks — that's why mid gets a strict < on whichever side it's on. So by the time we reach the range checks, target != nums[mid] is guaranteed. Including mid in a range (using <=) would be harmless but logically sloppy.
        # The endpoints touching the outer bounds (nums[l], nums[r]) are inclusive because those values are real candidates we haven't tested. The endpoint touching nums[mid] is exclusive because we already ruled mid out.
        # Why we can only range-check the SORTED half -> we NEVER test the broken half directly. We test the sorted half, and use ELIMINATION: if target isn't in the sorted half, go to the other. That's why every branch checks the sorted half's range, then sends the search to the other half in the else.
        # The nested if/else only DECIDES the direction — it doesn't add iterations. The two levels of nesting look expensive but are all O(1) comparisons. Don't confuse branching complexity (how many cases) with time complexity (how many iterations). We still halve every step.

