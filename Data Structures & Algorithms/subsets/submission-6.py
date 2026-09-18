class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # This is to collect all subsets (the final answer)
        result = []
        # This is the running subset we build up and tear down as we explore
        subset = []

        # Backtracking helper; i = the index of the element we're deciding on
        def backtrack(i):
            # Base case: decided on every element → subset is complete → record a copy and return
            if i == len(nums):
                result.append(subset.copy())
                return
            
            # Include nums[i]: add it to the current subset
            subset.append(nums[i])
            # Recurse to decide the next element (with nums[i] included)
            backtrack(i + 1)

            # Undo the include (backtrack): remove nums[i]
            subset.pop()
            # Recurse to decide the next element (with nums[i] excluded)
            backtrack(i + 1)

        # Start deciding from index 0
        backtrack(0)
        # Return all subsets
        return result


        # TC: O(n . 2ⁿ) -> there are 2ⁿ subsets to generate (each element in/out). for EACH subset, we do subset.copy() when recording it, which costs O(n) (copying up to n elements). 2ⁿ subsets × O(n) copy each = O(n · 2ⁿ).
        # SC: O(n) -> the recursion stack goes at most n deep (one frame per element) → O(n). The `subset` list holds at most n elements → O(n). Hence, O(n) extra space, NOT counting the output.


        # Solution Description: A subset is formed by deciding, for each element, whether to include it. With n elements, that's 2ⁿ possible subsets (each element is a yes/no choice). Backtracking explores all of them systematically. We walk through the elements one at a time, keeping a running subset. At each element we branch two ways: include it (add to subset, recurse), then exclude it (remove it — undo — and recurse). When we've decided on every element (reached the end), the current subset is one complete subset, so we record a copy. The "add, recurse, remove" rhythm is the backtracking heartbeat.


        # ----- Deep Dive -----

        # The backtracking rhythm — choose, recurse, un-choose -> The pattern: 1. make a choice (append), 2. explore all consequences of that choice (recurse), 3. UNDO the choice (pop) — this is "backtracking", 4. explore the alternative. The pop() is what makes it "backtracking" — after fully exploring the "include" branch, we RESTORE subset to its previous state so the "exclude" branch starts clean. Without the pop, nums[i] would leak into the exclude branch → wrong subsets.

        # Why subset.copy() and not just subset -> subset is ONE list that we keep mutating (append/pop) throughout the recursion. If we append subset itself (a reference), res holds many pointers to the SAME list. Later pops/appends change that list → all entries in res change! append subset (reference): res = [subset, subset, subset]  ← all point to the same list; after more mutations, subset = [] → res = [[], [], []]. append subset.copy(): res = [snapshot1, snapshot2, ...]  ← independent copies. Appending subset itself stores a reference — every entry in res would point to the same list and reflect later mutations (ending as identical garbage). A copy freezes a snapshot at that moment.

        # Why the base case is i == len(nums) -> We make one include/exclude decision per element. After deciding on ALL n elements (i has walked past the last index), the subset is complete. i goes 0, 1, 2, ..., n-1 (deciding each element) when i == n, there are no more elements to decide → subset is done → record it. Every path from the root to i == n represents one complete set of decisions = one subset. There are 2ⁿ such paths (2 choices × n elements). 

        # The decision-tree structure — why 2ⁿ subsets -> Each element is a branch point with 2 choices (include / exclude). So n elements give 2ⁿ leaves — exactly the number of subsets. No duplicates arise because each leaf is a unique sequence of yes/no decisions. This "each element is an independent binary choice" view is why the include/exclude structure is complete and duplicate-free.










