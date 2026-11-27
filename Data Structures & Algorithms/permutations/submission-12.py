class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # This is to collect all permutations
        result = []
        # The permutation being built
        perm = []
        # used[i] -> This bollean array tracks whether nums[i] is already placed in the current permutation
        used = [False] * len(nums)
        
        # Backtracking helper (no index parameter — we scan all elements every time)
        def backtrack():
            # Base case: permutation has all n elements → record a copy
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            # Consider every element (not just from a start index)
            for i in range(len(nums)):
                # Skip elements already used in the current permutation
                if used[i]:
                    continue

                # Choose nums[i]: add it to the permutation
                perm.append(nums[i])
                # Mark it used
                used[i] = True
                # Recurse to fill the next position
                backtrack()
                # Un-choose: unmark it (backtrack)
                used[i] = False
                # Remove it from the permutation
                perm.pop()
        
        # Start building
        backtrack()
        # Return all permutations
        return result


        # TC: O(n . n!) -> There are n! permutations to generate. For EACH permutation, we do perm.copy() when recording it → O(n). n! permutations × O(n) copy each = O(n · n!).
        # SC: O(n) -> recursion depth, the running perm, and the used array all scale with n. 


        # Solution Description: A permutation is an ordering of all n elements. Unlike combinations (where [1,2] and [2,1] are the same), here they're different — order matters. That changes the structure fundamentally. In combinations, a start index kept us moving forward (so we never revisited earlier elements, avoiding reorderings). But permutations want all reorderings — so we can't use a start index. Instead, at each position we consider every element that hasn't been used yet, tracked by a used boolean array. We build the permutation one position at a time: pick an unused element, mark it used, recurse to fill the next position, then unmark it (backtrack). When the permutation reaches length n, it's complete.


        # ----- Deep Dive -----

        # Why there's NO start index -> Combinations used a `start` index to only move FORWARD: for i in range(start, len(nums)) → this prevented reorderings ([1,2] but not [2,1]) → each combo once. Permutations WANT all reorderings ([1,2] AND [2,1] are both valid). So we must be able to pick ANY element at ANY position — including elements at indices BEFORE ones we've already picked. → we scan from 0 every time (for i in range(len(nums))), not from `start` → but now we need ANOTHER way to avoid picking the same element twice within one permutation → that's what `used` does. combinations: start index (forward-only) → no reorderings; permutations: no start index (any position) + used[] → all orderings, each element once.

        # Why we need the used array -> Since we scan ALL indices every time (no start index), we'd otherwise pick the same element repeatedly: perm = [1], then scan again from 0 → pick 1 again → [1,1] 💥. The `used` array prevents this: it marks which elements are ALREADY in the current permutation, so we skip them. used[i] == True  → nums[i] is already placed → skip it, used[i] == False → available → we can pick it. This ensures each element appears EXACTLY ONCE per permutation (which is what a permutation is — a rearrangement using every element once).

        # The paired mark/unmark — used[i] = True ... used[i] = False -> The used[i] = True / used[i] = False pair mirrors the append/pop — both pieces of state (the permutation and the used-flags) must be undone on backtrack. Forgetting used[i] = False would leave nums[i] permanently marked, so later branches couldn't use it, and you'd lose permutations. The unmark restores a clean state for the next choice.

        # Why the base case checks length, not an index -> Permutations check len(perm) == len(nums) (the permutation is full) rather than an index reaching the end. Combinations advance a single index through the array once → "done" when the index reaches the end.  Permutations have NO index — they build up `perm` by picking scattered elements → "done" when `perm` is full (has all n elements). len(perm) == len(nums) → every element has been placed → complete perm. Completeness is measured by how many elements we've placed, not how far an index has advanced.

        # Why there are n! permutations -> There are n! permutations because each position has one fewer choice than the last: n options for the first slot, n-1 for the second, and so on — n × (n-1) × ... × 1 = n!. This factorial growth (vs subsets' 2ⁿ) reflects that permutations make a shrinking choice per position rather than a binary in/out choice per element.








