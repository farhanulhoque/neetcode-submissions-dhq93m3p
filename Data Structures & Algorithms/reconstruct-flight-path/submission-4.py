class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)
        
        result = []

        def dfs(airport):
            while adj[airport]:
                nextDst = heapq.heappop(adj[airport])
                dfs(nextDst)
            result.append(airport)
        
        dfs("JFK")

        return result[::-1]