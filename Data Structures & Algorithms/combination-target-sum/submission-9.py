class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # This is to collect all valid combinations
        result = []
        # The running combination being built
        combo = []

        def backtrack(start, total):
            if total == target:
                result.append(combo.copy())
                return
            
            if total > target:
                return
            
            for i in range(start, len(nums)):
                combo.append(nums[i])
                backtrack(i, total + nums[i])
                combo.pop()
        
        backtrack(0, 0)
        return result
            

        # TC: 
        # SC: 


        # Solution Description: We build combinations by repeatedly choosing numbers, tracking the running sum. Two twists distinguish this from Subsets: Reuse: since a number can be picked unlimited times, after choosing nums[i] we recurse still allowing i (not i+1) — so we can pick it again. Avoiding duplicates: [2,2,3] and [3,2,2] are the same combination. To count each only once, we enforce a non-decreasing pick order via a start index: at each step we only consider elements from start onward, never going back to earlier indices. This means combinations are always built in index order, so no permutation of the same multiset is generated twice. We stop a branch when the sum hits the target (record it) or exceeds it (prune).


        # ----- Deep Dive -----

        # 






        
