class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        minHeap = [(0, k)]
        maxTime = 0
        visited = set()

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            maxTime = max(maxTime, time)            
            for nei, weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time + weight, nei))
        
        return maxTime if len(visited) == n else -1