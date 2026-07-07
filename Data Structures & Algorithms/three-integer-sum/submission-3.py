class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
        return result

        # TC: O(n^2) -> 
        # SC: O(1) -> 

        # Solution Description: Sort the array first. Then fix one element nums[i] at a time using an outer loop, and use two pointers l and r on the remaining subarray to find pairs that sum to -nums[i]. Sorting makes duplicate skipping trivial — if we see the same value as a previous iteration, we simply skip it. When a valid triplet is found, move both pointers inward and skip over any repeated values before the next comparison.

        # Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct. The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
        # Sorting is what makes duplicate skipping simple — equal values are always adjacent, so a single comparison nums[i] == nums[i-1] is all we need. Without sorting, detecting duplicates would require a Hash Set, costing extra space.
        # Why len(nums) - 2 -> The outer loop fixes nums[i] as the first element of the triplet. After fixing i, we need at least 2 more elements to the right for l and r. So i can never be the last element or second to last — it always needs at least 2 elements after it.