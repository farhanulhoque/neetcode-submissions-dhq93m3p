class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        
        # Store the grid dimensions
        rows, cols = len(grid), len(grid[0])
        # This is to track the largest island area found (starts at 0 → handles "no island")
        maxArea = 0

        # DFS helper that returns the area of the island reachable from (r, c)
        def dfs(r, c):
            # Boundary check: row or column out of the grid. Water check: this cell is water (0). If out of bounds or water, it contributes 0 area
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == 0):
                return 0
            
            # Sink this land cell to 0 (mark visited)
            grid[r][c] = 0

            # Count this cell as 1, then add the areas from all four directions
            return (1 + 
                    dfs(r - 1, c) + 
                    dfs(r + 1, c) + 
                    dfs(r, c - 1) + 
                    dfs(r, c + 1))
        
        # Scan every cell. If this cell is unvisited land, flood it, get its area, and update the maximum
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        
        # Return the largest island area
        return maxArea


        # TC: O(m . n) -> outer loop visits all m·n cells once. across all dfs calls, each cell is visited at most once (sunk after) → all flooding totals O(m·n).
        # SC: O(m . n) -> recursion stack depth can reach O(m·k) if the whole grid is one island (DFS recurses through all cells before unwinding). Sinking in place avoids a separate visited set. Returning the area adds no extra cost — it's folded into the same single traversal.


        # Solution Description: Scan every cell. On an unvisited land cell, run a DFS that returns the island's area: each land cell contributes 1 plus the areas returned by flooding its four neighbors. Sink cells as visited. Track the maximum returned area.


        # ----- Deep Dive -----

        # Why the DFS RETURNS the area (1 + four directions) -> Number of Islands' dfs returned nothing — it just sank cells. Here, the dfs RETURNS the area of the island it floods. The formula: THIS cell counts as 1, plus the area contributed by each of its four neighbors (recursively).
            # 1                → this cell
            # + dfs(r+1,c)     → area of everything reachable going down
            # + dfs(r-1,c)     → ... going up
            # + dfs(r,c+1)     → ... going right
            # + dfs(r,c-1)     → ... going left

            # Water/boundary neighbors return 0 (Line 6), contributing nothing. Land neighbors return THEIR subtree's area, which bubbles up. The areas ADD (not max) because every cell in the island is part of the SAME island — we want the TOTAL cell count, so we sum all contributions.
            # This is exactly like computing a TREE'S SIZE:
            # size(node) = 1 + size(left) + size(right)
            # area(cell) = 1 + area(each neighbor)
            # Each cell/node counts itself (1) and sums its children's counts. Same pattern.
        

        # Why we max across islands but sum within one -> Two levels, two operations:

            # WITHIN an island → SUM: every cell of ONE island adds to that island's
            #     total area. We want the full size, so we add all cells together.

            # ACROSS islands → MAX: we want the LARGEST island, so among all the
            #     island areas, we keep the biggest.

            # Don't confuse them:
            #     summing across islands → would give total land, not max island 
            #     maxing within an island → would give 1 (a single cell), not the area 

            # Sum to measure one island; max to compare islands.

        
        # Why maxArea = 0 handles the no-island case -> Initializing maxArea = 0 correctly handles "no island" — if the grid is all water, dfs never runs and 0 is returned. This works because areas are non-negative, so 0 is the right floor (contrast Max Path Sum, where negative values forced a non-zero initial value).






        