class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom-Up DP

        # dp[a] = fewest coins to make amount a; initialize all to amount + 1 (an “infinity” sentinel — larger than any real answer, since you’d never need more than amount coins)
        dp = [amount + 1] * (amount + 1)
        # Base case: dp[0] = 0 — zero coins make amount 0
        dp[0] = 0

        # Build up every amount from 1 to the target
        for a in range(1, amount + 1):
            # For each amount, try every coin denomination
            for c in coins:
                # Only use a coin if it fits (c <= a — can’t subtract more than you have)
                if c <= a:
                    # Taking coin c last means dp[a-c] + 1 coins; keep the minimum over all coins
                    dp[a] = min(dp[a], dp[a - c] + 1)
        
        # If dp[amount] was never improved (still the sentinel), it’s impossible → -1; else return it
        return dp[amount] if dp[amount] != amount + 1 else -1


        # TC: 
        # SC: 


        # Solution Description: Let dp[a] = the fewest coins needed to make amount a. To make amount a, the last coin you added was some coin c (from the denominations), which leaves a - c to make with the fewest coins — i.e. dp[a - c] + 1. We don’t know which last coin is best, so we try every coin and take the minimum: dp[a] = min over all coins c (where c <= a) of: dp[a - c] + 1. We build dp from amount 0 up to amount. Base case: dp[0] = 0 (zero coins make amount 0). Unreachable amounts stay at “infinity.” At the end, dp[amount] is the answer, or -1 if it’s still infinity (impossible). Because coins are unlimited, dp[a] can use dp[a - c] which may itself have used coin c — reuse is automatic.


        # ----- Deep Dive -----

        # Why dp is indexed by AMOUNT, not array position (the dimension shift) -> Previous 1-D DP problems indexed dp by POSITION in an input array (dp[i] = answer considering elements 0..i). Here, dp is indexed by AMOUNT OF MONEY:

                # dp[a] = fewest coins to make amount `a`.

                # The subproblems are "make amount 0", "make amount 1", ..., "make amount `amount`".
                # We build larger amounts from smaller ones.

                # This is a KEY generalization: the DP dimension isn't always "array index" — it can
                # be any quantity that has a natural "smaller subproblem" structure. Here, amount `a`
                # is built from amount `a - c` (a smaller amount).

                #     dp array has size amount+1 (indices 0 through amount), NOT len(coins).
                #     the number of COINS affects the transitions (which smaller amounts to try),
                #     not the dp dimension.
        


        # The recurrence — “try every coin as the last one” -> To make amount `a`, the LAST coin added was some coin `c`. After adding it, the remaining amount to make was `a - c`, which takes dp[a - c] coins at minimum. So using `c` as the last coin costs dp[a - c] + 1 (the +1 is coin c itself). 

                # We don't know which last coin is best, so we TRY EVERY coin and take the minimum:
                # dp[a] = min over all coins c (c <= a) of (dp[a - c] + 1).

                # unlike Climbing Stairs (fixed two options: step from i-1 or i-2), here the
                # number of options = the number of COINS. We loop over all of them and min.

                # "try all choices, take the best" is a core DP structure — when each subproblem
                # has multiple ways to build it, loop over the choices and min/max.

                # amount=6, coins=[1,3,4]:
                # dp[6] = min(dp[5]+1, dp[3]+1, dp[2]+1)  (last coin 1, 3, or 4)
                #     = min(using a 1, using a 3, using a 4) → the fewest-coins option.

        

        # Why unlimited reuse is automatic (the unbounded knapsack insight) -> Coins are UNLIMITED — you can use the same denomination many times. The DP handles this AUTOMATICALLY, without any special tracking:

                # dp[a] builds from dp[a - c]. But dp[a - c] itself may have used coin c (and
                # dp[(a-c)-c] before that, etc.). So a single coin c can be used repeatedly
                # across the chain of subproblems.

                # e.g. amount=6, coins=[3]: dp[3]=1 (one 3), dp[6]=dp[3]+1=2 (two 3's). The coin
                # 3 was used twice — automatically, because dp[6] reuses dp[3] which used a 3.

                # This is "unbounded" reuse: because we always consider ALL coins at EVERY amount
                # (no "don't reuse" restriction), a coin can appear any number of times in the
                # optimal solution.

                #     contrast: if each coin could be used ONCE (0/1 knapsack), we'd need a 2-D dp
                #     tracking which coins are used. Here, unlimited reuse keeps it 1-D.
        


        # Why the amount + 1 sentinel (not infinity, and why it detects impossibility) -> We initialize dp to amount + 1 as an "infinity" sentinel — a value LARGER than any possible real answer: The most coins you'd EVER need for amount `a` is `a` coins (all 1's, if a 1-coin exists). So any real answer is <= amount. Using amount + 1 as the sentinel means mit's always bigger than a real answer → min() never wrongly picks it over a valid option.

                # Why not float('inf')? amount + 1 works and avoids potential issues (and keeps it an
                # int). Both are fine; amount + 1 is a clean finite sentinel.

                # Detecting IMPOSSIBILITY:
                #     if dp[amount] is STILL amount + 1 at the end, no combination of coins made the
                #     amount → it's impossible → return -1.
                #     if dp[amount] was improved to a real (smaller) value, that's the answer.

                #     e.g. amount=7, coins=[5]: dp[7] can't be made (5 and 10... no) → stays amount+1
                #     → return -1.



        # ----- Edge Cases -----

        # amount = 0 -> dp[0] = 0 directly; loop doesn’t run for amount 0 → returns 0 (zero coins make 0).

        # Impossible amount (coins=[5], amount=3) -> No coin fits or combos reach 3 → dp[3] stays amount+1 → returns -1.

        # Coin larger than amount -> The c <= a check skips it — never subtracts more than available.

        # Coin equal to amount -> dp[amount] = dp[0] + 1 = 1 → one coin.


        # Visual Walkthrough

                # coins = [1, 3, 4], amount = 6

                # ── Initialize ──
                #     dp = [0, 7, 7, 7, 7, 7, 7]   (dp[0]=0, rest = amount+1 = 7 sentinel)
                #         0  1  2  3  4  5  6     (indices = amounts)

                # ── Build up each amount ──
                #     a=1: try coins ≤ 1: coin 1 → dp[1-1]+1 = dp[0]+1 = 1. dp[1]=1.
                #         dp = [0,1,7,7,7,7,7]
                #     a=2: coin 1 → dp[1]+1 = 2. dp[2]=2.
                #         dp = [0,1,2,7,7,7,7]
                #     a=3: coin 1 → dp[2]+1=3; coin 3 → dp[0]+1=1. min → dp[3]=1.
                #         dp = [0,1,2,1,7,7,7]   (one 3 beats three 1's)
                #     a=4: coin 1 → dp[3]+1=2; coin 3 → dp[1]+1=2; coin 4 → dp[0]+1=1. min → dp[4]=1.
                #         dp = [0,1,2,1,1,7,7]   (one 4)
                #     a=5: coin 1 → dp[4]+1=2; coin 3 → dp[2]+1=3; coin 4 → dp[1]+1=2. min → dp[5]=2.
                #         dp = [0,1,2,1,1,2,7]   (4+1 or 1+1+3, both 2 coins)
                #     a=6: coin 1 → dp[5]+1=3; coin 3 → dp[3]+1=2; coin 4 → dp[2]+1=3. min → dp[6]=2.
                #         dp = [0,1,2,1,1,2,2]   (two 3's = 2 coins)

                # ── Result ──
                #     dp[6] = 2 (not the sentinel 7) → return 2 

                # Fewest coins for 6: two 3's (3+3). Note greedy (take 4 first → 4+1+1 = 3 coins)
                # would be WORSE — the DP correctly found 2 by trying all coins at each amount.
                # Each dp[a] was the min over "last coin = 1, 3, or 4."






