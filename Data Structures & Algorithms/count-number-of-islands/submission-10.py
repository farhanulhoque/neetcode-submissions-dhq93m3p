class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS

        # Grid dimensions
        rows, cols = len(grid), len(grid[0])
        # Island counter
        count = 0

        # BFS helper to flood one island from (r, c)
        def bfs(r, c):
            # Create the queue
            q = deque()
            # Seed it with the starting cell
            q.append((r, c))
            # Sink the starting cell immediately (mark visited on enqueue)
            grid[r][c] = "0"

            # Process until the queue empties
            while q:
                # Dequeue the next cell (FIFO)
                row, col = q.popleft()
                # Iterate the four directional offsets
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    # Compute the neighbor's coordinates
                    nr, nc = dr + row, dc + col
                    # Bounds check on the neighbor. Land check: the neighbor is unvisited land
                    if (nr >= 0 and nc >= 0 and nr < rows and nc < cols and
                        grid[nr][nc] == "1"):
                        # Sink the neighbor (mark visited when enqueuing)
                        grid[nr][nc] = "0"
                        # Enqueue the neighbor for processing
                        q.append((nr, nc))
        
        # Scan every cell. If the cell is unvisited land, new island → increment. Flood the island with BFS.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        # Return the island count
        return count


        # TC: O(m . n) -> outer loop visits all m·n cells. Across all BFS floods, each cell is enqueued and dequeued at most once (sunk on enqueue → never re-added). Total BFS work = O(m·n). 
        # SC: O(min(m, n)) typical, O(m · n) worst case -> the QUEUE holds at most the "frontier" of the current BFS — the cells at the current expansion edge. Worst case (e.g. a grid that's all land), the frontier can be O(min(m,n)) for a square-ish fill, but can reach O(m·n) in pathological shapes. Commonly cited as O(min(m,n)) for the frontier vs DFS's O(m·k) depth.


        # Solution Description: Same structure, but flood each island with BFS (a queue) instead of recursion. On an unvisited land cell, increment the count, then BFS outward: enqueue the cell, and repeatedly dequeue a cell, sink it, and enqueue its unvisited land neighbors. BFS avoids deep recursion, so it won't hit a stack-overflow on huge islands.


        # ----- Deep Dive -----

        # Why mark visited WHEN ENQUEUING (not when dequeuing) -> We sink a neighbor THE MOMENT we enqueue it, not when we later dequeue it. Why it matters: a cell can be reached from MULTIPLE neighbors. If we only sank cells on dequeue, the same cell could be enqueued several times (by each of its land neighbors) before any dequeue sinks it → it'd be processed multiple times, and the queue could blow up. mark on ENQUEUE → each cell enqueued exactly ONCE → no duplicates, mark on DEQUEUE → a cell could be enqueued many times before processing. This is a universal BFS rule: mark visited at enqueue time.

        # Why the direction-offsets loop is cleaner for BFS -> Instead of four separate lines (like DFS's four recursive calls), BFS loops over the four directional OFFSETS: (1,0) down, (-1,0) up, (0,1) right, (0,-1) left. Adding (dr,dc) to the current (row,col) gives each neighbor. This is a common, compact way to express 4-directional movement — one loop instead of four statements.

        # This is the usual DFS-vs-BFS space tradeoff (depth vs width), and it's why BFS is safer for very large grids — it avoids deep recursion that could overflow the stack.





