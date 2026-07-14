class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        # TC: O(nlogn)
        # SC: O(n)

        # Solution Description: The key transformation: convert each car into its time to reach the target = (target - position) / speed. A car behind another will merge into it if it would arrive at the same time or sooner (it catches up and is then blocked). Sort cars by position descending (closest to target first) and process them in that order. Use a stack holding the arrival times of established fleets. For each car, if its arrival time is greater than the fleet ahead (stack top), it's slower and forms its own fleet — push it. If its time is less than or equal, it catches up and merges — don't push. The number of fleets is the final stack size.