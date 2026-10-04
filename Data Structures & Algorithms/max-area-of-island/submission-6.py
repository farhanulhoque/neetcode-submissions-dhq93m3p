class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS

        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            area = 0

            while q:
                row, col = q.popleft()
                area += 1
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    if (nr >= 0 and nr < rows and nc >= 0 and nc < cols and 
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea
