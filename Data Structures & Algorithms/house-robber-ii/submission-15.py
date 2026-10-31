class Solution:
    def rob(self, nums: List[int]) -> int:
        # The O(1)-space version (index-based, no slicing)

        n = len(nums)

        if n == 1:
            return nums[0]
        
        def robLinear(start, end):
            prev2 = 0
            prev1 = 0 

            for i in range(start, end):
                curr = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = curr
            
            return prev1
        
        return max(robLinear(1, n), robLinear(0, n-1))


        # Passing indices instead of slicing avoids the O(n) copy, giving O(1) space. The robLinear(start, end) iterates nums[start:end] directly. Functionally identical; just more space-efficient. A clean optimization to mention.