class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        used = [False] * len(nums)
        
        def backtrack(perm):
            if len(perm) == len(nums):
                result.append(perm.copy())

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                perm.append(nums[i])
                backtrack(perm)
                used[i] = False
                perm.pop()

        backtrack([])
        return result
