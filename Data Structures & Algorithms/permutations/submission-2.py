class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        used = [False] * len(nums)

        def backtrack():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                perm.append(nums[i])
                used[i] = True
                backtrack()
                used[i] = False
                perm.pop()

        backtrack()
        return result