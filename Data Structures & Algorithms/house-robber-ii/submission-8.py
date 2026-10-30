class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if len(nums) == 1:
            return nums[0]
        
        def robLinear(houses):
            prev2 = 0
            prev1 = 0

            for num in houses:
                curr = max(prev1, prev2 + num)
                prev2 = prev1 
                prev1 = curr
            
            return prev1
        
        return max(robLinear(nums[1:]), robLinear(nums[:-1]))