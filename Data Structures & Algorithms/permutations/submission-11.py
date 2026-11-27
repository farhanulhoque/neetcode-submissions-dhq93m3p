class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result =[]

        used = [False] * len(nums)

        def backtrack(perm):

            if len(perm) == len(nums):
                result.append(perm.copy())
                return 
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                perm.append(nums[i])
                used[i] = True
                backtrack(perm)
                perm.pop()
                used[i] = False
                
        
        backtrack([])
        return result
        
