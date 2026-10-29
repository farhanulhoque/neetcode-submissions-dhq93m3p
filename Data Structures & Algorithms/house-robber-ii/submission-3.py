class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:                                 # Line 1
            return nums[0]                                  # Line 2

        def robLinear(houses):                             # Line 3
            prev2, prev1 = 0, 0                            # Line 4
            for num in houses:                             # Line 5
                curr = max(prev1, prev2 + num)             # Line 6
                prev2 = prev1                              # Line 7
                prev1 = curr                               # Line 8
            return prev1                                   # Line 9

        return max(robLinear(nums[1:]),                    # Line 10
                robLinear(nums[:-1]))                   # Line 11