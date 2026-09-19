class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # This is to collect all valid combinations
        result = []
        # The running combination being built
        combo = []

        # Helper: start = lowest index we may still pick; total = running sum
        def backtrack(start, total):
            # Success: sum equals target → record a copy and return
            if total == target:
                result.append(combo.copy())
                return

            # Prune: sum exceeded target → this branch is dead, return
            if total > target:
                return
            
            # Try each candidate from start onward (never earlier — avoids duplicates)
            for i in range(start, len(nums)):
                # Choose nums[i]
                combo.append(nums[i])
                # Recurse with start = i (so nums[i] can be reused) and the updated sum
                backtrack(i, total + nums[i])
                # Un-choose (backtrack): remove nums[i]
                combo.pop()
        
        # Start: index 0, sum 0
        backtrack(0, 0)
        # Return all combinations
        return result
            

        # TC: 
        # SC: 


        # Solution Description: We build combinations by repeatedly choosing numbers, tracking the running sum. Two twists distinguish this from Subsets: Reuse: since a number can be picked unlimited times, after choosing nums[i] we recurse still allowing i (not i+1) — so we can pick it again. Avoiding duplicates: [2,2,3] and [3,2,2] are the same combination. To count each only once, we enforce a non-decreasing pick order via a start index: at each step we only consider elements from start onward, never going back to earlier indices. This means combinations are always built in index order, so no permutation of the same multiset is generated twice. We stop a branch when the sum hits the target (record it) or exceeds it (prune).


        # ----- Deep Dive -----

        # Why backtrack(i, ...) and not backtrack(i+1, ...) — enabling reuse -> Recursing with backtrack(i, ...) instead of i+1 is what permits reuse — after picking nums[i], index i is still available, so the same number can be chosen again. This single change (vs Subsets' i+1) is the difference between "each element once" and "unlimited repeats." If we used i+1 (like Subsets), each number could be used only once → we'd never build [2,2,2] → wrong for this problem.

        # Why the start index prevents duplicate combinations -> The rule: we only ever pick elements at index >= start. We never go BACK to an earlier index. This forces combinations to be built in NON-DECREASING index order: once you've moved past index i, you can't pick anything before i again. So each unique multiset is produced exactly ONCE, in index order. Duplicates (reorderings of the same numbers) are impossible.  Why passing `i` as the next start works: backtrack(i, ...) means "the next pick can be i or later, but not before i" → the combination's indices only stay the same or increase → no going back.

        # Why we pass i (not i+1) as the next start — reconciling reuse and uniqueness -> "i" (not i+1): the next pick can STILL be index i → REUSE allowed. "i" (not 0):   the next pick can't go BEFORE i → NO DUPLICATES. 1. if we passed i+1: no reuse (couldn't repeat nums[i]) 2.if we passed 0: duplicates (could pick earlier indices → reorderings) 3. passing i: the sweet spot — reuse without duplicates. 

        # The two base cases — success vs pruning -> 






        
