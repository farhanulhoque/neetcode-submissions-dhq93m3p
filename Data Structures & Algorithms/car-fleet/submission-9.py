class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleet = 0
        prevTime = 0

        for p, s in pair:
            time = (target - p) / s
            if time > prevTime:
                fleet += 1
                prevTime = time
            # else: merges into current fleet
        
        return fleet

        # TC: O(nlogn)
        # SC: O(n)

        # Instead of a stack, track just the last fleet's arrival time. A car forms a new fleet only if its time exceeds the current fleet's time. 