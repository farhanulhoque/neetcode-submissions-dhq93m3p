class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))

        # prefix starts at 1 — nothing to the left of index 0
        prefix = 1
        # Scan left to right, and at each index, store the product of everything to its left
        for i in range(len(nums)):
            # Store the running product of everything to the left of i into result[i]
            result[i] = prefix
            # Multiply prefix by nums[i] — expanding it rightward for next iteration
            prefix *= nums[i]
        
        # postfix starts at 1 — nothing to the right of last index
        postfix = 1
        # Scan right to left, and at each index, multiply in the product of everything to its right
        for i in range(len(nums) - 1, -1, -1):
            # Multiply output[i] by running product of everything to the right of i
            result[i] *= postfix
            # Expand suffix leftward for next iteration
            postfix *= nums[i]
        
        return result


        # TC: O(n) -> Two separate linear passes over nums
        # SC: O(1) -> No extra data structures — prefix and suffix are single integers. result array doesn't count as extra space since it's the required return value. 

        # We never store a separate prefix array or suffix array — we reuse result itself for the prefix pass, then multiply the suffix directly into it. 
