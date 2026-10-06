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
        
        # Scan every cell to find all treasures (multi-source BFS)
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
        

        # TC: O(m . n) -> the seeding loop scans all m·n cells once to find treasures → O(m·n). The BFS: each cell is enqueued at most ONCE (set to a distance on first visit → no longer INF → never re-enqueued), and each dequeue examines 4 neighbors (O(1)). So the BFS is O(m·k) total.
        # SC: O(m . n) -> the queue can hold up to O(m·n) cells in the worst case (e.g. many treasures seeded at once, or a wide BFS frontier). So O(m·n) for the queue in the worst case.

        # Contrast the naive per-cell BFS: O((m·n)²). Multi-source collapses it to a single O(m·n) pass — that's the big win.


        # Solution Description: We want each land cell's distance to its nearest treasure. The naive approach — BFS from every land cell to find the closest treasure — is expensive. The clever flip: BFS outward from all treasures at once. Seed a queue with every treasure cell (distance 0). Then BFS normally: dequeue a cell, and for each unvisited land neighbor (INF), set its distance to the current cell's distance + 1 and enqueue it. Because all treasures start together and BFS expands level by level, the first time any cell is reached, it's reached via the shortest path from the nearest treasure — so we set its distance once and never revisit. Water (-1) blocks the spread. Cells unreachable from any treasure stay INF.


        # ----- Deep Dive -----

        # Why multi-source BFS (seeding ALL treasures at once) -> NAIVE: for each land cell, BFS to find the nearest treasure → m·k land cells × O(m·k) BFS each = O((m·k)²) — slow. MULTI-SOURCE: seed the queue with ALL treasures at distance 0, then BFS outward ONCE. 
                # → the distances spread from every treasure simultaneously, like multiple ripples expanding and meeting. Each cell is claimed by the FIRST ripple to reach it — which comes from its NEAREST treasure.
                # → a single O(m·k) BFS solves ALL cells at once.

                # The flip: instead of "from each cell, find the nearest treasure," we do "from all treasures, spread to all cells." Same answer, vastly faster. It's the signature technique for "nearest source" problems.
        

        # Why the FIRST visit gives the shortest distance (if ... grid[nr][nc] == INF) -> BFS expands LEVEL BY LEVEL: all distance-1 cells are processed before any distance-2 cell, which are processed before any distance-3 cell, etc. So when BFS first REACHES a cell, it arrives via the shortest possible path (fewest steps) — from whichever treasure is nearest. The "grid[nr][nc] == INF" check ensures we only set a cell the FIRST time we reach it (it's still INF = untouched). Once set, it's no longer INF, so later (longer) paths to it are IGNORED. → first arrival = shortest distance = from nearest treasure.
            # This is BFS's defining property: in an unweighted graph, BFS visits nodes in order of increasing distance. The first visit is always the shortest.
            # Why not DFS? DFS plunges deep down one path — it might reach a cell via a LONG path first, recording the wrong (non-shortest) distance. BFS's level-order expansion is what guarantees shortest-first. DFS can't do this.
        

        # Why == INF serves triple duty -> This one condition simultaneously:

            #     1. SKIPS WATER (-1): water isn't INF, so the check fails → walls block the spread, as required.

            #     2. SKIPS TREASURES (0): treasures aren't INF → we never overwrite a treasure's 0 (they stay as sources).

            #     3. SKIPS ALREADY-VISITED cells: once a cell's distance is set (to some number ≥ 1), it's no longer INF → we don't revisit it (which also guarantees the first/shortest distance sticks).

            # So "== INF" means "an untouched, traversable land cell" — exactly the cells we should spread into. No separate visited set, no separate wall check needed.
        

        # Why unreachable cells stay INF automatically -> Unreachable cells stay INF automatically. The BFS only sets cells it can reach (spreading from treasures through traversable land). A cell walled off from all treasures is never dequeued's-neighbor, never set → stays INF. No special handling needed — "unreachable → stays INF" is the natural result of BFS only touching reachable cells. A land cell surrounded by -1 water on all sides: BFS never reaches it → it remains 2147483647.



        # ----- Edge Cases -----:

        # Empty grid -> The if not grid: return guard handles it — without it, grid[0] would crash on dimension lookup.

        # No treasures (all land/water) -> The seeding loop adds nothing to the queue; the BFS loop never runs; every land cell stays INF. Correct (no treasure to be near).

        # No land (all treasures/water) -> All treasures are seeded, but they have no INF neighbors to spread to, so the BFS does nothing. Grid is already "complete."

        # Land fully walled off by water -> BFS never reaches those cells → they stay INF, exactly as required for unreachable cells.

        # A cell adjacent to multiple treasures -> The first treasure's ripple to reach it (distance 1 from the nearest) sets it; the == INF check blocks any later, equal-or-longer path from overwriting. Nearest wins.

        # Single cell grid -> If it's a treasure (0), it stays 0 (no neighbors). If it's land (INF), it stays INF (no treasure). If water (-1), unchanged. All handled naturally.

        # Grid is all INF -> No sources seeded → nothing spreads → all stay INF. Correct.






