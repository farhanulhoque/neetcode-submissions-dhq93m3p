class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # DFS (with the n-1 edge check)

        if len(edges) != n - 1:
            return False
        
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        dfs(0)

        return len(visited) == n
        

        # Solution Descriptioin: A valid tree has two properties: it’s connected (every node reachable from any other) and acyclic (no cycles). There’s a beautiful shortcut: a graph with n nodes is a tree if and only if it has exactly n-1 edges and is connected. (With n-1 edges, connectivity automatically implies no cycle, and vice versa — the two conditions are linked.) So the cleanest check: first, if the edge count isn’t n-1, it can’t be a tree (too few → disconnected; too many → has a cycle). Then verify connectivity with a single traversal from node 0 — if it reaches all n nodes, it’s connected, and combined with n-1 edges, it’s a valid tree. We traverse DFS or BFS, tracking visited nodes and (for undirected graphs) avoiding the immediate parent back-edge.