class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result = nums[0]
        curMin = nums[0]
        curMax = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            candidates = (num, num * curMax, num * curMin)
            curMax = max(candidates)
            curMin = min(candidates)
            result = max(result, curMax)
        
        return result


        # TC: 
        # SC: 


        # Solution Description: 


        # ----- Deep Dive -----

        # 


        # ----- Edge Cases -----

        # 







