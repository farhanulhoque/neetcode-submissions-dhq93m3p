class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijkstra with a redefined “distance”

        # n = the grid’s side length
        n = len(grid)
        # Min-heap seeded with (grid[0][0], 0, 0) — the start cell; the time to “be” at the start is its own elevation
        minHeap = [(grid[0][0], 0, 0)]
        # Visited set — cells whose minimum reach-time is finalized
        visited = set()
        # Mark the start visited
        visited.add((0, 0))
        # The four directional offsets
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Dijkstra’s main loop: process until the heap empties
        while minHeap:
            # Pop the cell reachable at the lowest time (smallest max-elevation path)
            time, r, c = heapq.heappop(minHeap)
            
            # If this is the bottom-right cell, return the time — the first time we pop the target is the minimum
            if r == n - 1 and c == n - 1:
                return time
            
            # Explore each neighbor
            for dr, dc in directions:
                # Compute the neighbor’s coordinates
                nr, nc = r + dr, c + dc
                # Bounds check. Only consider unvisited neighbors.
                if (0 <= nr < n and 0 <= nc < n and
                    (nr, nc) not in visited):
                    # Mark the neighbor visited
                    visited.add((nr, nc))
                    # The modified cost: time to reach the neighbor = max(current time, neighbor's elevation). This is the max Elevation along this path so far. The lowest-possible maximum will be the answer.
                    newTime = max(time, grid[nr][nc])
                    # Push the neighbor with its reach-time
                    heapq.heappush(minHeap, (newTime, nr, nc))
            
        
        # TC: O(n² · log n) -> there are n² cells. Each is enqueued at most once (marked visited on enqueue) → up to O(n²) heap pushes/pops. Each heap operation is O(log(heap size)) = O(log(n²)) = O(2 log n) = O(log n). Each cell checks 4 neighbors (O(1)). O(n²) heap operations × O(log n) each = O(n² · log n).
        # SC: O(n²) -> the heap can hold up to O(n²) cells → O(n²). The visited set holds up to n² cells → O(n²). O(n²) total


        # Solution Description: You can be at a cell at time t only if water level t is at least every elevation on your path there (both squares of each step must be ≤ t). So the earliest time you can reach a cell equals the maximum elevation along the best path to it — and you want to minimize that maximum. This is a minimize-the-maximum (bottleneck) problem. It’s Dijkstra with a twist: instead of a path’s cost being the sum of edge weights, a path’s cost is the maximum cell elevation on it. We run Dijkstra from (0,0) with a min-heap keyed by “the max elevation needed to reach this cell so far.” We always expand the cell reachable at the lowest time, and when a neighbor is reached, the time to reach it is max(current time, neighbor's elevation). The first time we pop the bottom-right cell, that popped value is the answer.


        # ----- Deep Dive -----

        # Why the path cost is max, not sum (the core reframe) -> you can be at a cell at time t only if the water covers EVERY cell on your path (each ≤ t). So the EARLIEST time you can reach a cell via a path = the MAXIMUM elevation on that path (you must wait for the highest cell to be submerged). 
                # → a path's "cost" is its MAXIMUM cell, not its sum.
                # → to reach neighbor: newTime = max(time so far, neighbor's elevation).
                #   (you need the water to cover both where you are AND the neighbor → the max.)

                # This is "minimize the maximum" (bottleneck shortest path): among all paths to the target, find the one whose HIGHEST cell is as LOW as possible. That lowest- possible maximum is the answer.

                # Dijkstra: push (dist + weight, node)   ← sum
                # Here:     push (max(time, elevation), node)  ← max

                # Why max(time, elevation) and not just elevation? Because to reach the neighbor, the water must cover BOTH the path so far (which needed `time`) AND the neighbor (elevation). You need water ≥ both → ≥ max(time, elevation).

                # Standard Dijkstra: a path's cost = SUM of edge weights (accumulate). The time to reach a node = sum of weights along the path.
        

        # Why Dijkstra still works with a max-based cost -> Dijkstra still works because its greedy correctness only requires that extending a path never decreases its cost — and max(time, elevation) ≥ time satisfies this (the path-maximum can only stay the same or grow). So the first time we pop a cell, we’ve found its minimum-possible path-maximum, and it’s final — exactly like standard Dijkstra, with “lowest path-sum” replaced by “lowest path-maximum.” This is why Dijkstra generalizes to bottleneck problems.


        # Why the first pop of the target is the answer -> Dijkstra pops cells in increasing order of reach-time. The FIRST time we pop the bottom-right cell, `time` is the minimum max-elevation over all paths to it — i.e., the earliest time you can reach it. That's exactly the answer. We can return IMMEDIATELY on popping the target — no need to finish the whole grid. Any later path to the target would have a time ≥ this (we process in increasing-time order), so the first pop is optimal. The answer = the minimum, over all paths from (0,0) to (n-1,n-1), of the maximum elevation on the path = the first-popped time at the target.


        # Why seed the start with its own elevation -> The "time to be at the start cell" is grid[0][0] — you need the water to cover the start itself before you can be there (and begin swimming). So we seed the heap with (grid[0][0], 0, 0): the start's reach-time is its own elevation. Every subsequent cell's time builds via max(..., elevation) from there. 
                # If the start elevation is 5, you can't "be" at the start until time 5 → the path-maximum already includes the start → seed with grid[0][0].
                # Seeding with 0 would wrongly ignore that the start itself must be submerged.
        

        # Why mark visited on enqueue (and why it’s safe here) -> We mark a cell visited when we ENQUEUE it (not when we pop it). This is a valid Dijkstra variant here because:
                #  The FIRST time we enqueue a cell, it's reached via the lowest-time path found so far from an already-finalized (lower-time) cell. Since we process cells in increasing time order, the first enqueue is via an optimal-enough path, and we won't find a better one later. Marking on enqueue avoids pushing the same cell multiple times (The more common "mark on pop / skip if visited" variant also works; this problem's distinct elevations make mark-on-enqueue clean and correct.)



        # ----- Edge Cases -----

        # 1×1 grid -> Start is the target: pop (grid[0][0], 0, 0), r==n-1 and c==n-1 → return grid[0][0]. The time is just the single cell’s elevation.

        # Start or end has the highest elevation -> The answer is at least max(grid[0][0], grid[n-1][n-1]) — both must be submerged. The max cost naturally includes them.

        # Straight unobstructed path -> Dijkstra finds the path minimizing the peak elevation; the answer is that path’s maximum.

        # Monotonic grid (values increase toward the end) -> The bottom-right (highest) cell dominates → answer is its elevation (you must wait for it regardless of path).

        # Distinct values (guaranteed) -> No ties to worry about; the heap ordering is unambiguous.

        # Large grid -> O(n² log n) — efficient; the heap holds up to O(n²) cells.









