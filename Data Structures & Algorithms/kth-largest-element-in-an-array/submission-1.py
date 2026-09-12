class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k                                # Line 1  (kth largest = index k in ascending)

        def quickselect(left, right):                     # Line 2
            pivot = nums[right]                           # Line 3
            p = left                                       # Line 4

            for i in range(left, right):                  # Line 5
                if nums[i] <= pivot:                      # Line 6
                    nums[p], nums[i] = nums[i], nums[p]   # Line 7
                    p += 1                                 # Line 8

            nums[p], nums[right] = nums[right], nums[p]    # Line 9

            if p < k:                                      # Line 10
                return quickselect(p + 1, right)          # Line 11
            elif p > k:                                    # Line 12
                return quickselect(left, p - 1)           # Line 13
            else:                                          # Line 14
                return nums[p]                            # Line 15

        return quickselect(0, len(nums) - 1)              # Line 16