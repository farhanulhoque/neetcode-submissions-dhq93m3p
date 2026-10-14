class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(n))
        rank = [1] * n
        count = n

        def find(node):
            while node != parent[node]:
                node = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return 0
            
            if rank[pa] < rank[pb]:
                pa, pb = pb, pa
            parent[pb] = pa

            rank[pa] += rank[pb]

            return 1
        
        for a, b in edges:
            count -= union(a, b)
        
        return count
            