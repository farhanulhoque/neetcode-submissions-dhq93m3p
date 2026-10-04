class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS

        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = dr + row, dc + col
                    if (nr >= 0 and nc >= 0 and nr < rows and nc < cols and
                        grid[nr][nc] == "1"):
                        grid[nr][nc] = "0"
                        q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        
        return count