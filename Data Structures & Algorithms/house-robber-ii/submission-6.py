class Solution:
    def rob(self, nums: List[int]) -> int:
        # Two linear runs (reduction)

        # If there’s only one house, rob it (can’t exclude either endpoint when there’s only one — special case)
        if len(nums) == 1:
            return nums[0]

        # Helper: the linear House Robber on a given list of houses   
        def robLinear(houses):
            # Base cases: max robbable from no houses = 0 (both sliding variables)
            prev2 = 0
            prev1 = 0

            # Process each house’s money
            for num in houses:
                # The rob-or-skip decision: skip (prev1) or rob (prev2 + num) — take the larger
                curr = max(prev1, prev2 + num)
                # Slide the window: prev2 becomes the old prev1
                prev2 = prev1 
                # prev1 becomes the new curr
                prev1 = curr
            
            # Return the max robbable for this linear range
            return prev1
        
        # Case A: exclude house 0 → run linear House Robber on houses 1..n-1 (nums[1:]). Case B: exclude house n-1 → run linear House Robber on houses 0..n-2 (nums[:-1]); return the max of the two cases.
        return max(robLinear(nums[1:]), robLinear(nums[:-1]))


        # TC: 
        # SC: 


        # Solution Description: The only difference from House Robber is that house 0 and house n-1 are now adjacent (the circle), so you can’t rob both. The elegant insight: this means in any valid robbery, at least one of the two endpoints is NOT robbed. That gives two cases: Case A: don’t rob house 0 → rob freely among houses 1..n-1 (a linear row), Case B: don’t rob house n-1 → rob freely among houses 0..n-2 (a linear row). Each case is just the linear House Robber on a sub-range (which has no circular constraint, since we’ve dropped one endpoint). The answer is the max of the two cases. We reuse the exact House Robber helper twice. One edge case: a single house (no range to exclude) is handled directly.


        # ----- Deep Dive -----

        # The core insight — circular reduces to two linear runs -> 



        # ----- Edge Cases -----

        # 






