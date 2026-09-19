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


        # TC: 
        # SC: 


        # Solution Description: A permutation is an ordering of all n elements. Unlike combinations (where [1,2] and [2,1] are the same), here they're different — order matters. That changes the structure fundamentally. In combinations, a start index kept us moving forward (so we never revisited earlier elements, avoiding reorderings). But permutations want all reorderings — so we can't use a start index. Instead, at each position we consider every element that hasn't been used yet, tracked by a used boolean array. We build the permutation one position at a time: pick an unused element, mark it used, recurse to fill the next position, then unmark it (backtrack). When the permutation reaches length n, it's complete.


        # ----- Deep Dive -----

        # 







