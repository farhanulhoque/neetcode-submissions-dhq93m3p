class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        visited = set()
        minHeap = [(0, 0)]
        totalCost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            totalCost += cost

            xi, yi = points[i]
            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(minHeap, (dist, j))
        
        return totalCost