class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)]
        visited = set((0, 0))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            
            if r == n - 1 and c == n - 1:
                return time
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n and
                    (nr, nc) not in visited):
                    visited.add((nr, nc))
                    newTime = max(time, grid[nr][nc])
                    heapq.heappush(minHeap, (newTime, nr, nc))
