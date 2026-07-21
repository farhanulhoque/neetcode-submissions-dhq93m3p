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
                # Is the target within the left half's range [nums[l], nums[mid]). If Yes — search the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # target must be in the right half
                else:
                    left = mid + 1
            # Otherwise the right half [mid..r] is properly sorted
            else:
                # Is the target within the right half's range (nums[mid], nums[r]]. If Yes — search the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # target must be in the left half
                else:
                    right = mid - 1
        
        return -1

        # TC: O(logn) -> Each iteration halves the search space with O(1) comparisons. The extra branching decides direction, not count — still logarithmic
        # SC: O(1) -> Only l, r, mid — no extra structures

        # Solution Description: This fuses the sorted-half insight from Find Minimum with a target search. At each step, at least one half of the array is properly sorted. Determine which half is sorted by comparing nums[mid] to nums[l]. Then check whether the target lies within that sorted half's range — if yes, search there; if no, search the other half. The reasoning: we can only make a clean "is the target in this half?" decision on the sorted half, because its bounds are trustworthy (nums[l] to nums[mid], or nums[mid] to nums[r]). The broken half's bounds don't reliably bracket its contents, so we handle it by elimination — if the target isn't in the sorted half, it must be in the other.
        


