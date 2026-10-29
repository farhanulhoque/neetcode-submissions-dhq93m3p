class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Space-Optimized Bottom-Up

        # n = number of floors (the top is index n, just past the last)
        n = len(cost)

        # prev2 = min cost to reach floor i-2; starts at 0 (reaching floor 0 is free — you start there)
        prev2 = 0
        # prev1 = min cost to reach floor i-1; starts at 0 (reaching floor 1 is free — you can start there too)
        prev1 = 0

        # Compute the min cost to reach each floor from 2 up to the top (n)
        for i in range(2, n + 1):
            # Reaching floor i via a 1-step from i-1: cost to reach i-1 (prev1) + the cost paid at i-1 (cost[i-1]) or via a 2-step from i-2: cost to reach i-2 (prev2) + the cost paid at i-2 (cost[i-2]); take the cheaper
            curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            # Slide the window: prev2 becomes what prev1 was
            prev2 = prev1
            # prev1 becomes the newly computed curr
            prev1 = curr
        
        # After the loop, prev1 is the min cost to reach the top (index n)
        return prev1


        # TC: O(n) -> the loop runs from 2 to n → O(n) iterations. Each iteration does O(1) work (a min, an add, two assignments). O(n) overall.
        # SC: O(1) -> only three variables (prev2, prev1, curr) regardless of n. No array, no recursion. O(1) — the space-optimized form.

        # Full-array bottom-up would be O(n) space; this optimized version drops it to O(1) by keeping only the last two values.


        # Solution Description: We want the cheapest way to reach the top (index n, just past the last floor). To reach the top, your last step came from floor n-1 or floor n-2. More generally, the minimum cost to stand on floor i is cost[i] (to step off it) plus the cheaper of reaching i-1 or i-2: minCost(i) = cost[i] + min(minCost(i-1), minCost(i-2)). The base cases: floors 0 and 1 are free to start on (you choose either), so their minimum cost is just their own cost[0] and cost[1]. The top (index n) has no cost of its own — reaching it is min(minCost(n-1), minCost(n-2)). Since each value needs only the previous two, we keep two variables → O(1) space.


        # ----- Deep Dive -----

        # The recurrence — min instead of + (counting vs optimizing) -> Climbing Stairs COUNTED ways → it SUMMED the subproblems (ways from i-1 PLUS ways from i-2). This problem MINIMIZES cost → it takes the MIN of the choices.

                # To reach floor i, you arrived from EITHER i-1 (a 1-step) OR i-2 (a 2-step). You
                # want the CHEAPER arrival:
                #     - via i-1: (min cost to reach i-1) + (cost paid at i-1 to step off it)
                #     - via i-2: (min cost to reach i-2) + (cost paid at i-2 to step off it)
                #     → minCost(i) = min(these two).

                #     Counting → SUM (add both options' counts).
                #     Optimizing → MIN or MAX (pick the best single option).

                # This min-vs-sum distinction is THE difference between counting DP and
                # optimization DP. Same subproblem structure (depend on i-1, i-2), different
                # COMBINE step.


        # Why base cases are 0 (the “start free” insight) -> The problem says you may START at index 0 OR index 1. "Starting" there is FREE — you don't pay to be placed there; you only pay when you STEP OFF a floor. So the min cost to REACH floor 0 is 0 (you just start there), and to reach floor 1 is also 0 (you can start there too). Hence prev2 = prev1 = 0.

                # note the subtlety: cost[i] is paid when you STEP OFF floor i, not to reach
                # it. Reaching floors 0 and 1 is free (starting points); the costs kick in as
                # you climb past them.

                # If we wrongly set these to cost[0]/cost[1], we'd overcount — we'd pay to "reach"
                # a starting floor, which the problem says is free.
        

        # Why the loop goes to n (reaching the top “past the last index”) -> The "top" is index n — ONE PAST the last floor (which is index n-1). We must compute the cost to reach n, not just n-1.

                # So the loop runs to n inclusive (range(2, n+1)). When i = n:
                #     curr = min(prev1 + cost[n-1], prev2 + cost[n-2])
                #     = min cost to reach the top by stepping off floor n-1 or floor n-2.

                #     the top itself has NO cost (it's not a floor with a cost[] entry) — reaching
                #     it is purely the cost of the last step from n-1 or n-2.

                # If we only looped to n-1, we'd return the cost to reach the LAST FLOOR, not the
                # TOP → wrong (off by one). The "+1" in range(2, n+1) reaches the actual top.
        

        # Why indexing is cost[i-1] and cost[i-2] (not cost[i]) -> The indexing is cost[i-1] and cost[i-2] (not cost[i]) because i is a floor position that ranges up to n (the top), while cost[] only has indices 0..n-1. We reach floor i by stepping off floor i-1 or i-2, paying their costs. Using cost[i] would go out of bounds at the top (i=n) and charge the wrong floor. The offset reflects “you pay for the floor you depart, not the one you arrive at.”


        # ----- Edge Cases -----

        # Two floors (n=2) -> Loop runs once (i=2): curr = min(0 + cost[1], 0 + cost[0]) = min(cost[0], cost[1]) → the cheaper single floor to start on and step off.

        # Minimum input -> The problem guarantees n ≥ 2, so base cases prev1, prev2 = 0 always apply.








