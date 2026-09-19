class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort so duplicate values sit next to each other (essential for the skip rule)
        candidates.sort()
        # Result list
        result = []
        # the running combination
        combo = []

        # Helper: start = next index to consider; total = running sum
        def backtrack(start, total):
            # Success: sum equals target → record a copy
            if total == target:
                result.append(combo.copy())
                return
            
            # Prune: sum exceeded target → abandon this branch
            if total > target:
                return
            
            # Try each candidate from start onward
            for i in range(start, len(candidates)):
                # If this value equals the previous one and we're not at the first pick of this level (i > start), skip it
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Choose candidates[i]
                combo.append(candidates[i])
                # Recurse with i+1 (each element used at most once) and the updated sum
                backtrack(i + 1, total + candidates[i])
                # Un-choose (backtrack)
                combo.pop()

        # Start: index 0, sum 0 
        backtrack(0, 0)
        # Return all unique combinations
        return result


        # TC: O(n · 2ⁿ) -> In the worst case, each element is include-or-exclude → up to 2ⁿ combos explored (like Subsets). The skip rule and pruning CUT this substantially in practice. Each recorded combination costs O(n) to copy. Sorting is O(n log n) — dominated by the exponential search.
        # SC: O(n) -> recursion depth ≤ n (each level advances the index) → O(n) stack. the `combo` list holds at most n elements → O(n). So total is O(n). 


        # Solution Dexcription: This is Combination Sum, but with two changes: no reuse (each element at most once → recurse with i+1), and the input has duplicates. The duplicate input is the real problem. If candidates = [1,1,2] and we naively backtrack, we'd generate [1,2] twice — once using the first 1, once using the second — even though they're identical combinations. To prevent this, we sort the array (so duplicates are adjacent), then apply a skip rule: within a single recursion level, if the current element equals the previous one, skip it. This ensures each distinct value is only started once per level, eliminating duplicate combinations while still allowing genuine repeats that come from separate positions in the array. We stop a branch on success (sum == target) or prune (sum > target).


        # ----- Deep Dive -----

        # Why we must SORT first -> The skip rule works by comparing each element to its PREVIOUS one (candidates[i] == candidates[i-1]). For that comparison to catch ALL duplicates, identical values must be ADJACENT.Sorting groups duplicates together. 

        # The skip condition — if i > start and candidates[i] == candidates[i-1] -> The rule: "within THIS recursion level (this for-loop), don't START a combination with the same value twice." Two parts of the condition: 1. candidates[i] == candidates[i-1]  → this value is a duplicate of the prev, 2. i > start → we're NOT at the first iteration of this level. Why "i > start" and not "i > 0"? - We only skip duplicates at the SAME LEVEL. The FIRST time we see a value at this level (i == start), we MUST use it — that's a legitimate choice. We only skip the SECOND, THIRD, etc. occurrences at this level. ACROSS levels (going deeper), using the same value again is FINE — that's picking two different positions of a duplicate for one combination. WITHIN a level (the for loop), starting with the same value twice produces DUPLICATE combinations → skip.

        # Why i > start correctly allows genuine [1,1] combos but blocks duplicates -> The i > start check blocks only same-level duplicate starts (which would create identical combinations) while still allowing a duplicate value to be picked at a deeper level (which forms legitimate multi-copy combos like [1,1]). At a deeper level, the second 1 has i == start, so it's not skipped — it's a valid pick from a new position, not a reordering.

        # Why i+1 (not i) — no reuse -> Recursing with i+1 (not i) enforces each element used at most once — the next pick starts after the current position. Note "once" means once per position: two duplicate values at different positions can both be used (forming [1,1]), which is why we advance to the next position rather than banning the value. Position-level "use once" (i+1) and value-level dedup (the skip rule) are two separate mechanisms working together.

        # 







