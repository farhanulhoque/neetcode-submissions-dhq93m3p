class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combo = []

        def backtrack(i, total):
            if total == target:
                result.append(combo.copy())
                return
            
            if total > target:
                return
            
            for i in range(i, len(nums)):
                combo.append(nums[i])
                backtrack(i, total + nums[i])
                combo.pop()
        
        backtrack(0, 0)
        return result
            




        # Solution Description: 


        # ----- Deep Dive -----

        # 






        
