class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS

        # Grid dimensions
        rows, cols = len(grid), len(grid[0])
        # Tracks the largest island area
        maxArea = 0

        # BFS helper returning the area of the island from (r, c)
        def bfs(r, c):
            # Create the queue
            q = deque()
            # Seed it with the starting cell
            q.append((r, c))
            # Sink the starting cell (mark visited on enqueue)
            grid[r][c] = 0
            # This is the running area counter for this island
            area = 0

            # Process until the queue empties
            while q:
                # Dequeue the next cell
                row, col = q.popleft()
                # Count this cell toward the area
                area += 1
                # Iterate the four directional offsets
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    # Compute the neighbor's coordinates
                    nr, nc = row + dr, col + dc
                    # Bounds check on the neighbor. Land check: unvisited land. 
                    if (nr >= 0 and nr < rows and nc >= 0 and nc < cols and 
                        grid[nr][nc] == 1):
                        # Sink the neighbor (mark visited on enqueue)
                        grid[nr][nc] = 0
                        # Enqueue the neighbor
                        q.append((nr, nc))
            # Return this island's total area
            return area
        
        # Scan every cell. If unvisited land, flood it, get its area, update the max
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        # Return the largest area
        return maxArea


        # TC:
        # SC:


        # Solution Description: Flood each island with BFS, counting cells as we go. On an unvisited land cell, BFS outward: sink and enqueue the start, then repeatedly dequeue, increment an area counter, and enqueue unvisited land neighbors. Track the maximum area. BFS avoids deep recursion for very large islands.


        # ----- Deep Dive -----

        # 





        
