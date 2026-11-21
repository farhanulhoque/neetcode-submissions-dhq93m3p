class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its speed so they stay together when sorted
        pair = [[p, s] for p, s in zip(position, speed)]
        # Sort by position descending — closest to target processed first
        pair.sort(reverse=True)

        # This Stack is for holding arrival times of distinct fleets
        stack = []
        # Process each car from closest-to-target to farthest
        for p, s in pair:
            # Compute this car's time to reach the target
            time = (target - p) / s
            # Tentatively push its arrival time
            stack.append(time)

            # If there are ≥ 2 times and this car arrives at or before the fleet ahead, it merges — pop it back off (it's absorbed into the fleet ahead). 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        # Remaining stack entries are distinct fleets — return the count
        return len(stack)


        # TC: O(nlogn) -> Sorting dominates at O(n log n). The stack pass is O(n) — each car pushed once, popped at most once
        # SC: O(n) -> The pair array and stack each hold up to n elements


        # Solution Description: The key transformation: convert each car into its time to reach the target = (target - position) / speed. A car behind another will merge into it if it would arrive at the same time or sooner (it catches up and is then blocked). Sort cars by position descending (closest to target first) and process them in that order. Use a stack holding the arrival times of established fleets. For each car, if its arrival time is greater than the fleet ahead (stack top), it's slower and forms its own fleet — push it. If its time is less than or equal, it catches up and merges — don't push. The number of fleets is the final stack size.


        
        # ----- Deep Dive -----

        # Why sort by position descending? 

                # Cars can't pass each other (one lane). So whether a car forms its own fleet or joins
                # one depends ONLY on the cars AHEAD of it (closer to the target) — a car behind can
                # never affect a car in front.

                # Sorting by position DESCENDING processes cars from CLOSEST-to-target to FARTHEST. This
                # means when we process a car, all the cars AHEAD of it have already been processed —
                # so we know the "fleet situation" in front of it.

                #     target=12, cars at positions [10, 8, 5, 3]:
                #     sorted descending: position 10 first (closest to target), then 8, 5, 3.
                #     → we decide car-at-10's fleet, then car-at-8 (which might catch car-at-10), etc.

                # Why descending specifically? Because a car catches up to the one IN FRONT of it. To
                # know if car X joins a fleet, we need to have already figured out the fleet directly
                # ahead of X — which is the car at a HIGHER position. Processing highest-position-first
                # guarantees that.

                #     zip(position, speed) pairs each car's position with its speed; sorting the pairs
                #     sorts by position (the first element) automatically.



        # Why we compute arrival TIME, not position (the key metric) ->

                # The question isn't "where is each car?" but "does a car catch the fleet ahead before
                # reaching the target?" The right metric is ARRIVAL TIME:
                #     time = distance to target / speed = (target - pos) / spd.

                # A car catches the fleet ahead if it would arrive AT THE SAME TIME OR SOONER than that
                # fleet (if unobstructed). Here's the logic:
                #     - if car X (behind) has arrival time ≤ the fleet ahead's arrival time, X would
                #     reach the target at or before them — meaning X catches up to them on the way
                #     (since it can't pass, it joins and they travel together as one fleet).
                #     - if X's arrival time is GREATER (slower to arrive), it never catches them → X is
                #     its own separate fleet (possibly leading cars behind IT).

                #     e.g. target=12: car at pos 10, speed 2 → time (12-10)/2 = 1.0.
                #                     car at pos 8, speed 4 → time (12-8)/4 = 1.0.
                #     the pos-8 car arrives at time 1.0, same as the pos-10 car → it catches up → they
                #     form ONE fleet.

                # So we convert position+speed into a single comparable number: arrival time. The whole
                # problem becomes "compare arrival times of adjacent cars (in position order)."

                #     why time and not position? two cars at different positions with different speeds
                #     can't be compared by position alone — the faster one behind might or might not
                #     catch up. Arrival time captures BOTH position and speed in one number that directly
                #     answers "does it catch up?"



        # The stack and the merge condition (stack[-1] <= stack[-2]) -> 

                # The stack holds the arrival times of distinct FLEET LEADERS (cars that are, so far,
                # their own fleet). We process cars front-to-back (descending position).

                # For each new car (arrival time = stack[-1] after appending):
                #     compare it to the fleet directly ahead (stack[-2], the previously-processed car):
                #     - stack[-1] <= stack[-2]: this car arrives AT OR BEFORE the fleet ahead → it
                #     CATCHES UP and MERGES → pop it (it's not a separate fleet; it joins the one
                #     ahead, traveling at that fleet's slower pace).
                #     - stack[-1] > stack[-2]: this car arrives LATER (slower) → it NEVER catches the
                #     fleet ahead → it stays on the stack as its OWN fleet leader.

                #     the pop "absorbs" the car into the fleet ahead. After popping, the fleet ahead's
                #     arrival time (stack[-2], now stack[-1]) remains the fleet's defining time — because
                #     the merged car travels at the SLOWER (ahead) fleet's speed, arriving at that time.

                #     this is a MONOTONIC STACK: the arrival times on the stack stay in DECREASING order
                #     (each remaining leader arrives later than the one ahead of it). A car that would
                #     violate that (arrives sooner) gets merged/popped.

                # Why compare to stack[-2] (the car ahead), not further back? Because a car can only
                # directly catch the fleet IMMEDIATELY ahead of it (can't pass). If it merges, it takes
                # on that fleet's time; if a later car catches THIS merged fleet, it compares to that
                # same leading time. The stack's top always represents the nearest fleet ahead.



        # Why len(stack) at the end is the fleet count ->

                # After processing all cars, the stack contains exactly the arrival times of the distinct
                # FLEET LEADERS — each remaining entry is a fleet that stays separate all the way to the
                # target (it never caught the fleet ahead).

                # Cars that merged into a fleet ahead were POPPED (absorbed), so they're not counted.
                # What remains = the number of distinct fleets that reach the target.

                #     the stack's size directly answers "how many separate groups of cars arrive?" —
                #     which is the problem's question.

                #     e.g. if 5 cars collapse into 2 fleets (some caught up, some didn't), the stack ends
                #     with 2 entries → return 2.






        