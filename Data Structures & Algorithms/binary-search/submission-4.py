class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left and right bound the search space
        left, right = 0, len(nums) - 1

        # Keep searching while the range is non-empty. <= because l == r is still a valid one-element range.  l == r  →  exactly one element left — still needs checking!
        while left <= right:
            # Calculate the midpoint of the current rang
            mid = left + (right - left) // 2

            # Found it — return the index
            if nums[mid] == target:
                return mid
            # Middle is too small — target must lie to the right. Discard the left half and mid itself
            elif nums[mid] < target:
                left = mid + 1
            # Middle is too large — target must lie to the left. Discard the right half and mid itself
            else:
                right = mid - 1
        # Pointers crossed with no match — target not in the array
        return -1

        # TC: O(logn) -> Each iteration discards half the remaining range. Starting from n, we halve until 1 element remains — that's log₂(n) iterations, each doing O(1) work
        # SC: O(1) -> Just three integers (l, r, mid) — no extra structures, no recursion stack

        # Solution Description: Keep two pointers l and r bounding the portion of the array still worth searching. Look at the middle element. If it equals the target, we're done. If it's too small, the target must be to the right — move l past mid. If it's too large, the target must be to the left — move r before mid. Each comparison eliminates half the remaining candidates, so we reach the answer in log n steps. If the pointers cross without a match, the target isn't present.

        # Why mid = l + (r - l) // 2 and not (l + r) // 2 -> Both give the same answer in Python. The difference is integer overflow in fixed-width languages. Python's ints are arbitrary precision, so (l + r) // 2 never overflows here. But l + (r - l) // 2 is the habit interviewers look for — it signals you've thought about overflow.
        
            

