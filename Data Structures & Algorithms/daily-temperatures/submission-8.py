class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # This is the result array pre-filled with 0 (the default for days with no warmer future)
        result = [0] * len(temperatures)
        # This Stack is for holding indices of days awaiting a warmer temperature
        stack = []

        # Scan each day with its index i and temperature temp
        for i, temp in enumerate(temperatures):
            # While the stack is non-empty and today is warmer than the day on top of stack, pop that waiting day's index
            while stack and temp > temperatures[stack[-1]]:
                prevIndex = stack.pop()
                # Its answer is the gap: i - prevIndex days until warmer
                result[prevIndex] =  i - prevIndex
            # Push today's index — it now waits for its own warmer day
            stack.append(i)
        
        return result

        # TC: O(n) -> Each index is pushed once and popped once across the entire run. The while looks nested but total pops ≤ n — amortized O(1) per day
        # SC: O(n) -> The stack holds up to n indices (e.g. a strictly decreasing temperature array where nothing ever gets popped until the end)
        

        # Solution Description: For each day we want the distance to the next warmer day. This is the classic "next greater element" problem, solved with a monotonic decreasing stack of indices. We scan left to right, keeping a stack of days that are still waiting for a warmer temperature. When the current day is warmer than the day at the top of the stack, we've found that day's answer — pop it and record the day gap (current index - popped index). We keep popping while the current day is warmer than the stack's top, since one warm day can resolve multiple waiting days. Days that never get a warmer future day stay at 0 (the default).


        # ----- Deep Dive -----

        # Why the stack holds INDICES of days "waiting" for a warmer day ->

                # As we scan left to right, some days haven't yet found a warmer day to their right —
                # they're "waiting." The stack holds the INDICES of these waiting days (not their
                # temperatures — we store indices so we can both look up the temp AND compute the day
                # gap).

                #     a day goes on the stack when we see it (we don't yet know its answer).
                #     it comes OFF the stack when we later find a day warmer than it (its answer is
                #     resolved — that warmer day is what it was waiting for).

                # Why indices, not temperatures? Two reasons:
                #     1. we need the temperature → temperatures[stack[-1]] looks it up by index.
                #     2. we need the DAY GAP → i - prevIdx (the answer) requires the index, not the temp.

                #     so the index gives us both the value (via lookup) and the position (for the gap).

                # The stack is a BACKLOG of days still searching for their "next warmer day." Each day
                # enters the backlog when seen and leaves when resolved.

                #     temps [73, 74, ...]: push index 0 (73 waiting). see 74 (index 1): 74 > 73 → index 0
                #     resolved (waited 1 day). Then push index 1 (74 now waiting for something warmer).
        


        # Why the stack stays MONOTONICALLY DECREASING (the invariant) ->

                # The stack's temperatures (by index) are always in DECREASING order from bottom to top.
                # Here's why: before pushing a new day, we POP every day on the stack that's COOLER than
                # the current day (the while loop). So whatever remains is ≥ the current temp, and then
                # we push the current day on top.

                #     this keeps the stack decreasing: each new element is placed only after removing all
                #     smaller elements below it... wait, above it (at the top). The top is always the
                #     smallest-so-far among the waiting days.

                # Why does this invariant hold / matter?
                #     - a day can only be "resolved" by the FIRST warmer day to its right. Days further
                #     down the stack (cooler, earlier) are still waiting for THEIR warmer day.
                #     - when a warm day arrives, it resolves ALL the cooler days on top of the stack (all
                #     of them were waiting, and this day is warmer than all of them) — popping them off
                #     in order.
                #     - the decreasing order guarantees that once we hit a day on the stack that's ≥ the
                #     current temp, we STOP (that day isn't resolved yet — current isn't warmer than it).

                #     temps [75, 71, 69, 72]: 
                #     push 75, push 71 (71<75, stack decreasing: [75,71]), push 69 ([75,71,69]).
                #     see 72: pop 69 (69<72, resolved), pop 71 (71<72, resolved), stop at 75 (75≥72).
                #     push 72 → [75, 72]. still decreasing. ✓

                # The decreasing invariant is WHY each warm day cleanly resolves a contiguous run of
                # cooler waiting days from the top.



        # Why res[prevIdx] = i - prevIdx (the day gap) ->

                # When the current day i is warmer than the day at prevIdx (just popped), prevIdx's
                # "next warmer day" IS day i. The number of days it waited is the difference in their
                # indices:
                #     res[prevIdx] = i - prevIdx.

                #     prevIdx = 2, i = 6: the day at index 2 had to wait until index 6 for a warmer day →
                #     6 - 2 = 4 days. ✓

                # Why i - prevIdx and not just 1? Because the warmer day might be SEVERAL days later —
                # the gap is the actual number of days between them. Index subtraction gives exactly that.

                #     this is WHY we stored indices on the stack (Tricky Part 1): we need prevIdx to
                #     compute the gap. If we'd stored temperatures, we couldn't compute how many days
                #     apart they are.

                # Each popped day gets its answer at the MOMENT it's resolved — we don't revisit it. The
                # first warmer day to its right is found exactly when that warmer day is being processed.
        


        # Why days left on the stack keep their answer of 0 ->

                # Some days NEVER find a warmer day to their right (e.g. the hottest day, or days at the
                # end that only have cooler/equal days after). These days are never popped off the stack —
                # they remain "waiting" when the scan ends.

                # We handle them by INITIALIZING res to all 0s. A day that's never resolved keeps its
                # default 0, which is exactly the required answer ("0 if there's no warmer day ahead").

                #     temps [76, 73] at the end: 76 never gets a warmer day → stays on the stack → res[6]
                #     keeps its default 0. 73 (last day) → stays → res[7] = 0. ✓

                # So we don't need to explicitly handle the leftover stack — the all-0 initialization
                # covers "no warmer day found." The stack simply has unresolved days in it when we
                # finish, and their res entries are already correct (0).

                #     this is why res = [0]*n up front: it pre-fills the "no answer" case, and we only
                #     OVERWRITE entries for days that DO get resolved.
        


        # Why each element is pushed and popped at most once (the O(n) key) ->

                # At first glance, a for loop with a nested while loop looks like O(n²). But it's O(n)
                # because of AMORTIZED analysis:

                #     each day's index is PUSHED onto the stack exactly ONCE (the append at the end of
                #     each iteration).
                #     each index is POPPED at most ONCE (once popped/resolved, it never returns to the
                #     stack).

                #     so across the ENTIRE run, the total number of pops is at most n (one per element),
                #     and the total pushes is exactly n. The while loop's pops, summed over all iterations,
                #     total ≤ n — NOT n per iteration.

                #     → total work = n pushes + ≤ n pops + n iterations = O(n).

                # The while loop can pop MANY elements in a single iteration (when a very warm day
                # resolves a long run of cool days), but those elements are then GONE — they won't be
                # popped again. The "expensive" iterations are balanced by cheap ones. That's amortized
                # O(1) per element → O(n) total.

                # This "each element pushed/popped once → O(n) despite nested loops" is the signature
                # complexity argument for monotonic stacks.




        # Visual Walkthrough

                # temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
                # index:           0   1   2   3   4   5   6   7

                # res = [0, 0, 0, 0, 0, 0, 0, 0]   (all 0 to start)
                # stack = []   (holds indices; I'll show temps in parens for clarity)

                # ═══════════════════════════════════════════════

                # ── i=0, temp=73 ──
                #     stack empty → while loop doesn't run.
                #     push index 0.
                #     stack = [0(73)]
                #     res = [0,0,0,0,0,0,0,0]

                # ── i=1, temp=74 ──
                #     stack top = index 0 (73). 73 < 74? YES → pop index 0.
                #         res[0] = i - prevIdx = 1 - 0 = 1   (day 0 waited 1 day for warmer)
                #     stack now empty → while stops.
                #     push index 1.
                #     stack = [1(74)]
                #     res = [1,0,0,0,0,0,0,0]   ← res[0] resolved

                # ── i=2, temp=75 ──
                #     stack top = index 1 (74). 74 < 75? YES → pop index 1.
                #         res[1] = 2 - 1 = 1   (day 1 waited 1 day)
                #     stack empty → stop.
                #     push index 2.
                #     stack = [2(75)]
                #     res = [1,1,0,0,0,0,0,0]   ← res[1] resolved

                # ── i=3, temp=71 ──
                #     stack top = index 2 (75). 75 < 71? NO → while doesn't run (71 isn't warmer than 75).
                #     push index 3.
                #     stack = [2(75), 3(71)]   ← still decreasing: 75 > 71 ✓
                #     res = [1,1,0,0,0,0,0,0]

                # ── i=4, temp=69 ──
                #     stack top = index 3 (71). 71 < 69? NO → while doesn't run.
                #     push index 4.
                #     stack = [2(75), 3(71), 4(69)]   ← decreasing: 75 > 71 > 69 ✓
                #     res = [1,1,0,0,0,0,0,0]

                # ── i=5, temp=72 ──
                #     stack top = index 4 (69). 69 < 72? YES → pop index 4.
                #         res[4] = 5 - 4 = 1   (day 4 waited 1 day)
                #     stack top = index 3 (71). 71 < 72? YES → pop index 3.
                #         res[3] = 5 - 3 = 2   (day 3 waited 2 days)
                #     stack top = index 2 (75). 75 < 72? NO → stop.
                #     push index 5.
                #     stack = [2(75), 5(72)]   ← decreasing: 75 > 72 ✓
                #     res = [1,1,0,2,1,0,0,0]   ← res[3] and res[4] resolved in ONE iteration!

                # ── i=6, temp=76 ──
                #     stack top = index 5 (72). 72 < 76? YES → pop index 5.
                #         res[5] = 6 - 5 = 1   (day 5 waited 1 day)
                #     stack top = index 2 (75). 75 < 76? YES → pop index 2.
                #         res[2] = 6 - 2 = 4   (day 2 waited 4 days)
                #     stack empty → stop.
                #     push index 6.
                #     stack = [6(76)]
                #     res = [1,1,4,2,1,1,0,0]   ← res[2] and res[5] resolved; 76 cleared the whole stack

                # ── i=7, temp=73 ──
                #     stack top = index 6 (76). 76 < 73? NO → while doesn't run.
                #     push index 7.
                #     stack = [6(76), 7(73)]   ← decreasing: 76 > 73 ✓
                #     res = [1,1,4,2,1,1,0,0]

                # ═══════════════════════════════════════════════

                # ── Scan done. Leftover stack = [6(76), 7(73)] ──
                #     these days NEVER found a warmer day to their right → they keep their default 0:
                #     res[6] = 0 (76 was the hottest; nothing warmer after)
                #     res[7] = 0 (last day; nothing after)

                # return res = [1, 1, 4, 2, 1, 1, 0, 0] 




