class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        combo = []

        def backtrack(start, total):
            if total == target:
                result.append(combo.copy())
                return
            
            if total > target:
                return
            
            for i in range(start, len(nums)):
                combo.append(nums[i])
                backtrack(i, nums[i] + total)
                combo.pop()
        
        backtrack(0, 0)
        return result