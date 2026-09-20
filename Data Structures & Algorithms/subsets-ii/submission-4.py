class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        subset = []

        def backtrack(start):
            result.append(subset.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return result
        