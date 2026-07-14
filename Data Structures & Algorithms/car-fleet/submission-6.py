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

            # If there are ≥ 2 times and this car arrives at or before the fleet ahead, it merges — pop it back off (it's absorbed into the fleet ahead)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        # Remaining stack entries are distinct fleets — return the count
        return len(stack)

        # TC: O(nlogn) -> Sorting dominates at O(n log n). The stack pass is O(n) — each car pushed once, popped at most once
        # SC: O(n) -> The pair array and stack each hold up to n elements

        # Solution Description: The key transformation: convert each car into its time to reach the target = (target - position) / speed. A car behind another will merge into it if it would arrive at the same time or sooner (it catches up and is then blocked). Sort cars by position descending (closest to target first) and process them in that order. Use a stack holding the arrival times of established fleets. For each car, if its arrival time is greater than the fleet ahead (stack top), it's slower and forms its own fleet — push it. If its time is less than or equal, it catches up and merges — don't push. The number of fleets is the final stack size.