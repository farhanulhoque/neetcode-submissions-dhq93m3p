class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS (multi-source)
        
        # Guard: if the grid is empty -> nothing to do, return
        if not grid:
            return 
        
        # Store the grid dimensions
        rows, cols = len(grid), len(grid[0])
        # The INF sentinel value (traversable, unvisited land)
        INF = 2147483647
        # The BFS queue
        q = deque()
        
        # Scan every cell to find all treasures
        for r in range(rows):
            for c in range(cols):
                # If this cell is a treasure (0), seed the queue with it (all treasures are sources, distance 0)
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # process until the queue empties
        while q:
            # Dequeue the next cell
            row, col = q.popleft()
            # Iterate the four directional offsets
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                # Compute the neighbor's coordinates
                nr, nc = row + dr, col + dc
                # Bounds check on the neighbor. Only spread into unvisited land (INF) — skips water and already-set cells
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF):
                    # Set the neighbor's distance to this cell's distance + 1
                    grid[nr][nc] = grid[row][col] + 1
                    # Enqueue the neighbor to continue spreading
                    q.append((nr, nc))
        

        # TC: 
        # SC:


        # Solution Description: We want each land cell's distance to its nearest treasure. The naive approach — BFS from every land cell to find the closest treasure — is expensive. The clever flip: BFS outward from all treasures at once. Seed a queue with every treasure cell (distance 0). Then BFS normally: dequeue a cell, and for each unvisited land neighbor (INF), set its distance to the current cell's distance + 1 and enqueue it. Because all treasures start together and BFS expands level by level, the first time any cell is reached, it's reached via the shortest path from the nearest treasure — so we set its distance once and never revisit. Water (-1) blocks the spread. Cells unreachable from any treasure stay INF.


        # ----- Deep Dive -----

        # Why multi-source BFS (seeding ALL treasures at once) -> 






