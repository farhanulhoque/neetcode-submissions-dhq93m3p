class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            
            if rank[pa] < rank[pb]:
                pa, pb = pb, pa
            parent[pb] = pa
            rank[pa] += rank[pb]

            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
