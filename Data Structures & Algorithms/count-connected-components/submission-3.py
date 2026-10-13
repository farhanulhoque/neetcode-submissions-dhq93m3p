class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union-Find

        parent = list(range(n))
        rank = [1] * n
        count = n

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
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



        # TC:
        # SC: 


        # Solution Description: start with n components (every node isolated in its own set). Each edge tries to union its two endpoints. If they’re in different sets, the union merges them — two components become one, so the count drops by one. If they’re already in the same set (the edge is redundant), nothing changes. After processing all edges, the count is the number of connected components.


        # ----- Deep Dive -----

        # UNION-FIND tracks groups that merge over time:

            #     parent[]   → stores the pointer structure; parent[x] is x's immediate
            #                 parent. A self-pointing node is a leader (group representative).

            #     find(x)    → climb parent pointers up to the leader. Tells you x's group.
            #                 (path compression flattens the chain as it climbs)

            #     union(a,b) → find both leaders; point one at the other → merge the groups.
            #                 (union by rank attaches the smaller tree under the bigger)

            #     same leader (find(a)==find(b)) → already connected
            #                 → in a tree check: a cycle. in component count: redundant edge.

            # The whole thing: GROUPS identified by LEADERS, with two optimizations keeping
            # the leader always close by for speed.
        

        # 


        # ----- Edge Cases -----

        # 






