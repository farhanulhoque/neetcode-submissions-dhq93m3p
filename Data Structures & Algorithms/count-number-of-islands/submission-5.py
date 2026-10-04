class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Store the grid dimensions
        rows, cols = len(grid), len(grid[0])
        # Counter for the number of islands
        count = 0

        # DFS helper that floods one island from cell (r, c)
        def dfs(r, c):
            # Boundary check: row or column out of the grid. Water check: this cell is water ('0') — nothing to flood
            if (r < 0 or r >= rows or
                c < 0 or c >= cols  or
                grid[r][c] == "0"):
                return
            
            # Mark this land cell visited by sinking it to '0'
            grid[r][c] = "0"

            # Flood the neighbors (up, down, left, right)
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        # Scan every cell. # If the cell is unvisited land ('1'), it's a new island → increment the count. Flood the entire island so it's not counted again  
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
                    
        # Return the total island count
        return count


        # TC: O(m . n) -> the outer loop touches every cell once, and the flood-fills collectively visit each cell at most once (sunk cells are skipped), so total work is linear in the grid size.
        # SC: O(m . n) -> worst case for the recursion stack — if the whole grid is one island, the DFS can recurse through all cells before unwinding. Sinking in place avoids a separate visited set (O(1) extra for marking).


        # Solution Description: Scan every cell. On an unvisited land cell, increment the island count and run a DFS that recursively visits all connected land cells, marking each as visited (here, by sinking it to '0'). The DFS spreads depth-first through the island until no unvisited land remains.


        # ----- Deep Dive -----

        # Why each outer-loop land cell is a NEW island (counting connected components) -> The outer scan visits every cell. Crucially, dfs() SINKS every cell of an island to '0' as it floods. So by the time the scan moves on, the whole misland reads as water. When the scan later finds a '1', it CANNOT be part of an already-counted island (those are all '0' now). It must be a BRAND-NEW island. So every '1' the outer loop encounters is the first cell of an unvisited island → count it, then flood it away. The number of times we LAUNCH a dfs = the number of islands (connected components). The flood ensures each component is launched from exactly once.

        # Why sinking to '0' serves as "visited" -> We need to avoid revisiting cells (or the DFS would loop forever between adjacent lands). Instead of a separate visited set, we OVERWRITE land with water — same "mark in the grid" trick from Word Search's "#". Once a cell is '0', the water check (Line 7) stops any future visit to it → sinking = marking visited, using the grid itself. This mutates the input grid. If that's not allowed, use a separate `visited` set of (r,c) — but sinking saves O(m·n) space.

        # Why the flood-fill reaches the WHOLE island -> From a land cell, we recurse into all 4 neighbors. Each land neighbor recurses into ITS neighbors, and so on — the recursion spreads outward through every connected land cell. land → its land neighbors → their land neighbors → ... → the entire connected region, until every cell hits water or a boundary. This is why ONE dfs(r,c) call floods the COMPLETE island: the recursion transitively visits everything reachable via 4-directional land connections. Water cells and boundaries stop the spread, naturally outlining the island.








