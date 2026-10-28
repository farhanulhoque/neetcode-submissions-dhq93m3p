class Solution:
    def climbStairs(self, n: int) -> int:
        # Space-Optimized Bottom-Up
        
        if n <= 2:
            return n
        
        prev2 = 1
        prev1 = 2

        for i in range(3, n + 1):
            curr = prev2 + prev1
            prev2 = prev1
            prev1 = curr
        
        return prev1


        # TC:
        # SC: 


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



        # ----- Edge Cases -----

        # 
        