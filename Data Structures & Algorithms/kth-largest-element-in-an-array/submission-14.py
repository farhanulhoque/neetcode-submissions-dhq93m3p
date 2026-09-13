class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quickselect (Avg O(n) but worst case O(n^2))

        k = len(nums) - k

        def quickselect(left, right):
            pivot = nums[right]
            p = left

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p], nums[right] = nums[right], nums[p]

            if p < k:
                return quickselect(p + 1, right)
            elif p > k:
                return quickselect(left, p - 1)
            else:
                return nums[p]
        
        return quickselect(0, len(nums) - 1)
            


        # Solution Description: Pick a pivot, partition the array so smaller elements go one side and larger the other. After partitioning, the pivot is in its final sorted position. If that position is the one we want (the kth largest), we're done; otherwise recurse into just one side. Because we only recurse into one half each time, it's O(n) on average.

        