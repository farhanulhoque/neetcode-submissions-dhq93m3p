class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort so duplicates are adjacent (required for the skip rule)
        nums.sort()
        # Result list
        result = []
        # the running subset
        subset = []

        # Helper: start = lowest index we may still pick
        def backtrack(start):
            # Record the current subset at every node — every prefix is a valid subset
            result.append(subset.copy())

            # Try each candidate from start onward
            for i in range(start, len(nums)):
                # if this value repeats the previous one at this level (i > start), skip it
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Choose nums[i]
                subset.append(nums[i])
                # Recurse with i+1 (each element at most once)
                backtrack(i + 1)
                # Un-choose (backtrack)
                subset.pop()
        
        # Start from index 0
        backtrack(0)
        # Return all unique subsets
        return result


        # TC: O(n · 2ⁿ) -> worst case (all distinct), there are 2ⁿ subsets. Each recorded subset costs O(n) to copy. 2ⁿ subsets × O(n) copy each = O(n · 2ⁿ). With duplicates, the skip rule produces FEWER than 2ⁿ subsets, so it's faster in practice — but the worst case (distinct inputs) is O(n · 2ⁿ). Sorting is O(n log n) — dominated by the exponential term.
        # SC: O(n) -> recursion depth ≤ n (each level advances the index) → O(n) stack. The `subset` list holds at most n elements.


        # Solution Description: This is Subsets, but the input has duplicates — so we must avoid producing the same subset twice (e.g. from [1,1,2], don't list [1,2] twice using different 1s). The fix is exactly the recipe from Combination Sum II: sort the array so duplicates are adjacent, then skip same-level duplicates with the if i > start and nums[i] == nums[i-1]: continue rule. The structure uses a start index (each element at most once, recurse with i+1). One notable feature of subset generation: we record a subset at every node of the recursion (every prefix is a valid subset), not only at the leaves. Combined with the skip rule, this generates every unique subset exactly once.


        # ----- Deep Dive -----

        # Why we record at EVERY node (not just leaves) -> In Combination Sum, we recorded only when total == target (a specific  condition at the leaves). Here, EVERY subset is valid — [], [1], [1,2], etc. Every node in the recursion tree represents a valid subset (the current prefix). So we record at the TOP of every call, before the loop. Each recursive call = one subset. Recording at entry captures all 2ⁿ (deduped) subsets, including the empty one and all partial ones. 

        # The skip rule — identical to Combination Sum II -> It skips same-level duplicate starts (preventing duplicate subsets like two copies of [1,2]) while still allowing a duplicate value at a deeper level (forming genuine multi-copy subsets like [1,1]). The i > start distinction — first-at-level allowed, later-at-level skipped.

        # Why sorting is required -> Sorting is required so duplicates are adjacent, enabling the nums[i] == nums[i-1] comparison to catch them. Without it, scattered duplicates evade the skip rule and produce duplicate subsets.

        # There's no explicit i == len(nums) base case because the for loop provides it implicitly — when start reaches len(nums), range(start, len(nums)) is empty, the loop body never runs, no further recursion happens, and the call returns on its own. This works specifically because this version records at every node (every prefix is a subset), so it doesn't need to reach a leaf to know when to record. The original Subsets recorded only at leaves, so it needed the explicit base case. Both are correct; the for-loop style just folds termination into the loop's natural end. 
        
        # for i in range(start, n) backtracking loop is self-terminating — you only need an explicit base case when you must do something specific at the end (like record only at a leaf, or check a target). When every node is a valid answer and you record on entry, the empty range handles termination for free.






        
