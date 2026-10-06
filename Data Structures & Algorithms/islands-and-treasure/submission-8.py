class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        if not grid:
            return 
        
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            row, col = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF):
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))
            