class Solution:
    def climbStairs(self, n: int) -> int:
        # Space-Optimized Bottom-Up
        
        # For n = 1 or n = 2, the answer is n itself (1 way for 1 step; 2 ways for 2 steps: 1+1 or 2)
        if n <= 2:
            return n
        
        # prev2 (i - 2) = ways to reach step 1 = 1 (two steps back from where we start computing)
        prev2 = 1
        # prev1 (i - 1) = ways to reach step 2 = 2 (one step back)
        prev1 = 2
        
        # Compute ways starting from step 3 up to n
        for i in range(3, n + 1):
            # curr -> Ways to reach step i = ways to reach i-1 (prev1) + ways to reach i-2 (prev2)
            curr = prev2 + prev1
            # Slide the window: prev2 becomes what prev1 was
            prev2 = prev1
            # prev1 becomes the newly computed curr
            prev1 = curr
        
        # After the loop, prev1 holds the ways to reach step n
        return prev1


        # TC: O(n) -> the loop runs from 3 to n → O(n) iterations. Each iteration does O(1) work (one addition, two assignments). O(n) overall.
        # SC: O(1) -> only three variables (prev2, prev1, curr) regardless of n. No array, no recursion stack. O(1) — the space-optimized form.

        # Contrast: naive recursion is O(2ⁿ) time; bottom-up with a full array is O(n) time and O(n) space; this optimized version is O(n) time and O(1) space.


        # Solution Description: To reach step n, your last move was either a 1-step (from step n-1) or a 2-step (from step n-2). So the number of ways to reach step n is the ways to reach n-1 plus the ways to reach n-2: ways(n) = ways(n-1) + ways(n-2). That’s the Fibonacci recurrence! The base cases: ways(0) = 1 (one way to “climb” zero steps — do nothing) and ways(1) = 1 (one way — a single step). Because each value only depends on the previous two, we don’t even need a full array — we keep two variables and slide them up, giving O(n) time and O(1) space.


        # ----- Deep Dive -----

        # Dynamic Programming: 

                # Core Idea: solve a problem by breaking it into smaller overlapping subproblems, and remember each subproblem’s answer so you never recompute it.

                # DP applies when a problem has TWO properties:
                #     1. OVERLAPPING SUBPROBLEMS: the same smaller problems get solved over and
                #     over. (If subproblems were all distinct, plain recursion would suffice —
                #     no need to "remember.")

                #     2. OPTIMAL SUBSTRUCTURE: the answer to the big problem can be built from the
                #     answers to smaller subproblems. (The pieces combine into the whole.)

                # DP = recursion + REMEMBERING (so you don't resolve the same subproblem twice).

                # Two ways to implement DP:
                #         TOP-DOWN (Memoization):
                #             write the natural recursion, but CACHE each subproblem's answer in a map/array.
                #             before computing a subproblem, check the cache; if it's there, return it.
                #             → "recursion that remembers."

                #         BOTTOM-UP (Tabulation):
                #             start from the SMALLEST subproblems and build UP to the answer, filling a
                #             table (array) iteratively. No recursion — just a loop.
                #             → "build the answers from the ground up."
                # Both compute the same thing. Top-down is often easier to derive (just add a cache to recursion); bottom-up is often more efficient (no recursion overhead) and lets you optimize space.


                # Watch a problem go from a slow naive recursion to a fast DP:
                # STAGE 1 — Naive recursion (exponential, slow):
                #     ways(n) = ways(n-1) + ways(n-2)   ← to reach step n, you came from n-1 or n-2
                #     but this recomputes the SAME subproblems exponentially → O(2ⁿ). Terrible.

                # STAGE 2 — Top-down memoization (add a cache):
                #     same recursion, but store ways(i) in a cache. Each subproblem solved ONCE
                #     → O(n). The cache eliminates the recomputation.

                # STAGE 3 — Bottom-up tabulation (build a table):
                #     fill dp[0], dp[1], dp[2], ... up to dp[n] iteratively. O(n) time, O(n) space.

                # STAGE 4 — Space-optimized (keep only what you need):
                #     notice dp[i] only needs dp[i-1] and dp[i-2] → keep just TWO variables.
                #     O(n) time, O(1) space. The final, optimal form.

                # This 4-stage journey — naive → memoize → tabulate → optimize space — is the ARC
                # of nearly every DP problem. Climbing Stairs shows all four clearly.

                # THE DP RECIPE (how to approach a DP problem):
                #     1. Define the subproblem: what does dp[i] MEAN?
                #     2. Find the recurrence: how does dp[i] build from smaller subproblems?
                #     3. Set the base cases.
                #     4. Decide the order (bottom-up) or add memoization (top-down).
                #     5. Optimize space if dp[i] only needs recent entries.

                # once you have the DP framework, the question becomes “what’s the recurrence and is it count/min/max?
        


        # Deriving the recurrence — why ways(n) = ways(n-1) + ways(n-2) -> The recurrence ways(n) = ways(n-1) + ways(n-2) comes from: your last move to reach step n was either a 1-step (from n-1) or a 2-step (from n-2). These are the ONLY two ways to arrive at n (you climb 1 or 2 at a time). And they're mutually exclusive (distinct last moves). So:
                # ways(n) = ways(n-1) + ways(n-2)
                # (total ways = ways ending in a 1-step + ways ending in a 2-step)

                # the ways to reach n-1 and the ways to reach n-2 are the SUBPROBLEMS. The big answer (ways to reach n) is their SUM — optimal substructure. This is EXACTLY the Fibonacci recurrence.
        


        # Why naive recursion is exponential (and why DP fixes it) -> 
                # def climbStairs(n):
                #     if n <= 2: return n
                #     return climbStairs(n-1) + climbStairs(n-2)

                # This recomputes the SAME subproblems over and over. Consider climbStairs(5):
                #     climb(5) = climb(4) + climb(3)
                #     climb(4) = climb(3) + climb(2)   ← climb(3) computed AGAIN
                #     climb(3) = climb(2) + climb(1)   ← and AGAIN

                #     climb(3) is computed multiple times; climb(2) even more. The call tree
                #     BRANCHES exponentially → O(2ⁿ) calls. For n=50, that's ~10¹⁵ calls.

                # This is the OVERLAPPING SUBPROBLEMS property — the same subproblems recur. DP
                # fixes it by REMEMBERING each subproblem's answer (compute each once):
                #     → memoization (cache) or tabulation (table) → O(n).

                # The exponential-to-linear speedup IS why DP matters.
        


        # The space optimization — why only two variables (not a full array) -> A bottom-up DP would use a full array: dp[i] = dp[i-1] + dp[i-2], size n. But notice: computing dp[i] only ever needs dp[i-1] and dp[i-2] — the TWO most recent values. We NEVER look further back.

                # So we don't need the whole array — just two variables that SLIDE UP:
                #     prev2 (two back), prev1 (one back) → compute curr → slide:
                #         prev2 = prev1, prev1 = curr.

                #     → O(1) space instead of O(n). We keep a "window" of the last two answers.

                # This "only the last few values matter → keep variables, not an array" trick is
                # a RECURRING DP space optimization. Whenever dp[i] depends only on a fixed number
                # of recent entries, you can drop the array.
        

        # Why the base cases are ways(1)=1, ways(2)=2 -> 
                # if n <= 2:
                #     return n
                # prev2 = 1    # ways(1)
                # prev1 = 2    # ways(2)


                # Base cases anchor the recurrence (you can't recurse below them):

                #     ways(1) = 1: one step → only one way to get here(a single 1-step).
                #     ways(2) = 2: two steps → two ways to get here: [1,1] or [2].

                # From these, the recurrence builds everything: ways(3)=ways(2)+ways(1)=2+1=3, etc.

                # Getting base cases right is crucial in DP — a wrong base case propagates errors
                # through the whole table. Here, ways(1)=1 and ways(2)=2 are the foundation the
                # Fibonacci build rests on.

                # (Note: some formulations use ways(0)=1 — "one way to climb zero steps: do
                # nothing." That also works and makes ways(2)=ways(1)+ways(0)=1+1=2 consistent.)


        # ----- Edge Cases -----

        # Large n -> O(n) time, O(1) space — handles large n efficiently (no recursion depth issues, no overflow in Python).

        # n = 0 (if allowed) -> Not typical here (n ≥ 1 usually assumed); with ways(0)=1 formulation, returns 1.






        