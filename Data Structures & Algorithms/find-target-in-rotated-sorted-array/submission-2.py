class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
                
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

        # TC: O(logn)
        # SC: O(1)

        # Solution Description: This fuses the sorted-half insight from Find Minimum with a target search. At each step, at least one half of the array is properly sorted. Determine which half is sorted by comparing nums[mid] to nums[l]. Then check whether the target lies within that sorted half's range — if yes, search there; if no, search the other half. The reasoning: we can only make a clean "is the target in this half?" decision on the sorted half, because its bounds are trustworthy (nums[l] to nums[mid], or nums[mid] to nums[r]). The broken half's bounds don't reliably bracket its contents, so we handle it by elimination — if the target isn't in the sorted half, it must be in the other.
        


