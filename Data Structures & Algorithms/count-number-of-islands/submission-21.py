class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    
                    if (nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == "1"):
                        grid[nr][nc] = "0"
                        q.append((nr, nc))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
            
        return count