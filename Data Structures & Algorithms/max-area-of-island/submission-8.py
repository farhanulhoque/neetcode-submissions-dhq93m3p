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


        # TC:
        # SC:


        # Solution Description: Scan every cell. On an unvisited land cell, run a DFS that returns the island's area: each land cell contributes 1 plus the areas returned by flooding its four neighbors. Sink cells as visited. Track the maximum returned area.


        # ----- Deep Dive -----

        # 







        