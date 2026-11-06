class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev2 = 0
        prev1 = 0

        for i in range(len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1 
            prev1 = curr
        
        return prev1