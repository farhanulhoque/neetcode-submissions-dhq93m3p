class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array — enables two pointers and duplicate skipping
        nums.sort()
        result = []

        # Fix nums[i] as the first element - only go uo to len - 2 since we need at least 2 elements i.
        for i in range(len(nums) - 2):
            # If this value is the same as the previous i, it would produce duplicate triplets. Skip it — move to the next unique value of nums[i].
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Place left pointer just after i and right pointer at the end 
            left, right = i + 1, len(nums) - 1
            # keep going until pointers meet
            while left < right:
                # Compute the sum of all 3 elements
                total = nums[i] + nums[left] + nums[right]
                # Sum too small — need a bigger number
                if total < 0:
                    left += 1
                # Sum too large — need a smaller number
                elif total > 0:
                    right -= 1
                else:
                    # Add the valid triplet to result list
                    result.append([nums[i], nums[left], nums[right]])
                    # Move left and right pointers inward to look for more triplets
                    left += 1
                    right -= 1
                    # If the new nums[left] is the same value as the one we just used, skip it
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # If the new nums[right] is the same value as the one we just used, skip it
                    # while left < right and nums[right] == nums[right + 1]:
                    #     right -= 1
            
        return result

        # TC: O(n^2) -> Outer loop runs n times, two pointer inner loop runs n times — total n × n = O(n²). Sorting costs O(n log n) which is dominated by O(n²)
        # SC: O(1) -> This excludes the space used by the sorting algorithm and the result list.

        # Solution Description: Sort the array first. Then fix one element nums[i] at a time using an outer loop, and use two pointers l and r on the remaining subarray to find pairs that sum to -nums[i]. Sorting makes duplicate skipping trivial — if we see the same value as a previous iteration, we simply skip it. When a valid triplet is found, move both pointers inward and skip over any repeated values before the next comparison.

        # Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct. The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
        # Sorting is what makes duplicate skipping simple — equal values are always adjacent, so a single comparison nums[i] == nums[i-1] is all we need. Without sorting, detecting duplicates would require a Hash Set, costing extra space.
        # Why len(nums) - 2 -> The outer loop fixes nums[i] as the first element of the triplet. After fixing i, we need at least 2 more elements to the right for l and r. So i can never be the last element or second to last — it always needs at least 2 elements after it.

        # Why O(n^2) ->  Each outer iteration independently kicks off a fresh two pointer scan over the remaining subarray. The inner loop doesn't share its work across outer iterations — it resets and runs independently each time. In bucket sort, all inner iterations shared a total of n — each element was visited exactly once across everything. Each number is part of every subarray to its right — so it gets visited once per outer iteration that precedes it. In bucket sort, the outer and inner loops divide the work. In 3Sum, the outer and inner loops multiply the work.
