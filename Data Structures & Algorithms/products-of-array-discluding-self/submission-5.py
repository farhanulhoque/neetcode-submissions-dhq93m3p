class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))

        prefix = 1
        # Scan left to right, and at each index, store the product of everything to its left
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        # Scan right to left, and at each index, multiply in the product of everything to its right
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result

        # TC: O(n) -> Two separate linear passes over nums
        # SC: O(1) -> No extra data structures — prefix and suffix are single integers. Output array doesn't count as extra space since it's the required return value. 

        # We never store a separate prefix array or suffix array — we reuse output itself for the prefix pass, then multiply the suffix directly into it. 
