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
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        # Remaining stack entries are distinct fleets — return the count
        return len(stack)

        # TC: O(nlogn) -> Sorting dominates at O(n log n). The stack pass is O(n) — each car pushed once, popped at most once
        # SC: O(n) -> The pair array and stack each hold up to n elements

        # Solution Description: The key transformation: convert each car into its time to reach the target = (target - position) / speed. A car behind another will merge into it if it would arrive at the same time or sooner (it catches up and is then blocked). Sort cars by position descending (closest to target first) and process them in that order. Use a stack holding the arrival times of established fleets. For each car, if its arrival time is greater than the fleet ahead (stack top), it's slower and forms its own fleet — push it. If its time is less than or equal, it catches up and merges — don't push. The number of fleets is the final stack size.
        
        # Why sort by position descending? -> By processing closest-first, each new car we consider is BEHIND the fleets already on the stack. We only need to check if it catches the fleet immediately ahead of it. If we sorted ascending, a car would need to look forward at cars ahead — but those aren't on the stack yet. Descending order puts the "car ahead" on the stack before the car behind is processed.
        # stack[-1] = the car we JUST pushed (farther from target, BEHIND), stack[-2] = the fleet AHEAD of it (closer to target). If behind car's time <= ahead fleet's time: the behind car arrives at the same moment or sooner. If behind car's time > ahead fleet's time: it's slower, arrives later, never catches up → it stays as its OWN fleet → keep on stack. <= (not <) is required to satisfy the "catches up at the exact moment" rule.
        # Why this counts as a monotonic stack -> The stack ends up holding arrival times in strictly increasing order from bottom to top. Any car that would break the increasing order (time <= fleet ahead) gets merged (popped). So survivors always have strictly increasing times.