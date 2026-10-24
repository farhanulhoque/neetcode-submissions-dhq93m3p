class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)                                      # Line 1
        minHeap = [(grid[0][0], 0, 0)]                      # Line 2
        visited = set()                                     # Line 3
        visited.add((0, 0))                                # Line 4
        directions = [(1,0),(-1,0),(0,1),(0,-1)]           # Line 5

        while minHeap:                                      # Line 6
            time, r, c = heapq.heappop(minHeap)            # Line 7
            if r == n - 1 and c == n - 1:                  # Line 8
                return time                                # Line 9
            for dr, dc in directions:                      # Line 10
                nr, nc = r + dr, c + dc                    # Line 11
                if (0 <= nr < n and 0 <= nc < n            # Line 12
                        and (nr, nc) not in visited):       # Line 13
                    visited.add((nr, nc))                  # Line 14
                    newTime = max(time, grid[nr][nc])      # Line 15
                    heapq.heappush(minHeap, (newTime, nr, nc))  # Line 16