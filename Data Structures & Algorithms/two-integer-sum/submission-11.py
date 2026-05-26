class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numMap:
                # Since numMap[diff] was stored before i, it's always the smaller index first
                return [numMap[diff], i]
            # If not found yet, store this number and its index for future lookups
            numMap[n] = i
        
        # TC: O(n), Single pass through the array
        # SC: O(n), numMap dict can grow up to n entries


        
