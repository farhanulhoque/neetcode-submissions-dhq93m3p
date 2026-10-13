class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # DFS (with the n-1 edge check)

        # Quick reject: a tree with n nodes has exactly n-1 edges — if not, it can’t be a tree
        if len(edges) != n - 1:
            # Return false immediately (too few → disconnected; too many → has a cycle)
            return False
        
        # Build an adjacency list (undirected, so each edge goes both ways)
        adj = {i: [] for i in range(n)}
        # For each edge [a, b], add b as a neighbor of a and a as a neighbor of b (undirected)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # Set of visited nodes
        visited = set()

        # DFS helper to traverse the connected component from node
        def dfs(node):
            # Mark the current node visited
            visited.add(node)
            # Explore each neighbor
            for nei in adj[node]:
                # If a neighbor is unvisited, recurse into it.
                if nei not in visited:
                    dfs(nei)
        # Traverse starting from node 0
        dfs(0)

        # Connected iff the DFS reached all n nodes → valid tree (given n-1 edges)
        return len(visited) == n


        # TC: O(V + E) -> the edge-count check: O(1). building the adjacency list: O(V + E). DFS visits each node once and each edge once → O(V + E). O(V + E) overall. The n-1 shortcut makes this very efficient — a single traversal suffices.
        # SC: O(V + E) -> adjacency list: O(V + E). visited set: O(V). recursion stack: up to O(V) deep.


        # Solution Descriptioin: A valid tree has two properties: it’s connected (every node reachable from any other) and acyclic (no cycles). There’s a beautiful shortcut: a graph with n nodes is a tree if and only if it has exactly n-1 edges and is connected. (With n-1 edges, connectivity automatically implies no cycle, and vice versa — the two conditions are linked.) So the cleanest check: first, if the edge count isn’t n-1, it can’t be a tree (too few → disconnected; too many → has a cycle). Then verify connectivity with a single traversal from node 0 — if it reaches all n nodes, it’s connected, and combined with n-1 edges, it’s a valid tree. We traverse DFS or BFS, tracking visited nodes and (for undirected graphs) avoiding the immediate parent back-edge.


        # ----- Deep Dive -----

        # Why n-1 edges + connected = tree (the key theorem) -> THE THEOREM: for a graph with n nodes, ANY TWO of these three imply the third:
                # (1) connected
                # (2) acyclic (no cycles)
                # (3) exactly n-1 edges

                # So a tree (connected + acyclic) ALWAYS has exactly n-1 edges. And conversely, a graph with n-1 edges that is connected MUST be acyclic (hence a tree).
                # Why n-1 edges is the magic number:
                #     - a tree with n nodes needs exactly n-1 edges to connect them (each new
                #       node after the first adds exactly one edge to join the tree).
                #     - FEWER than n-1 edges → can't connect all n nodes → DISCONNECTED.
                #     - MORE than n-1 edges → an extra edge creates a CYCLE.
                #     - EXACTLY n-1 edges → if connected, no room for a cycle → it's a tree.

                # So checking "n-1 edges" + "connected" is sufficient — we don't even need a separate cycle check! The edge count + connectivity together force acyclicity.
        

        # Why the n-1 check lets us skip cycle detection -> Normally, validating a tree means checking BOTH "no cycle" AND "connected." But the n-1 edge count collapses this: IF we have exactly n-1 edges AND the graph is connected, THEN it's automatically acyclic (a cycle would require an extra edge, which would leave some node disconnected — contradicting connectivity). So after confirming n-1 edges, a SINGLE connectivity check (does DFS reach all n nodes?) is enough. We skip the (otherwise necessary) cycle detection. Without the n-1 shortcut, we'd need to detect cycles during traversal (via the parent-tracking trick — see the alternative), which is more work.

        # Why connectivity = DFS reaches all n nodes -> A graph is CONNECTED if every node is reachable from any starting node. We DFS from node 0 and mark everything reachable.
                # if the DFS reaches all n nodes (len(visited) == n) → connected 
                # if it reaches fewer → some nodes are in a separate component → DISCONNECTED 

                # Starting from node 0 is arbitrary — in a connected graph, a traversal from ANY node reaches all others. If node 0's component doesn't include everything, the graph isn't connected.
                # 0—1—2  3    (dfs(0) reaches {0,1,2}, misses 3 → len(visited)=3 ≠ 4 → not connected → not a tree)
        

        # Why undirected adjacency needs both directions -> An undirected edge [a, b] means a and b are mutually connected — you can traverse from a to b AND from b to a. So we add each to the OTHER's neighbor list. If we only did adj[a].append(b), we could reach b from a but NOT a from b → the traversal would miss paths → wrongly report disconnection. Undirected graphs ALWAYS store edges both ways in the adjacency list. (This differs from the directed Course Schedule graphs, where edges went one way.)



        # ----- Edge Cases -----

        # Single node, no edges (n=1, edges=[]) -> len(edges)=0 == n-1=0 ✓; dfs(0) visits {0}; len(visited)=1 == n → True. A single node is a valid tree.

        # No nodes (n=0) -> len(edges)=0 == n-1=-1? No (0 != -1) → returns False. (Edge case convention varies; some define n=0 as valid — clarify with the interviewer.)

        # Disconnected (too few edges) -> len(edges) < n-1 → fails the Line 1 check immediately → False.

        # Has a cycle (too many edges) -> len(edges) > n-1 → fails Line 1 → False. The extra edge means a cycle.

        # Exactly n-1 edges but disconnected - Passes Line 1, but DFS reaches fewer than n nodes → len(visited) != n → False. (This happens when n-1 edges form a cycle in one part, leaving another part disconnected — e.g. a triangle + isolated node.)

        # Self-loop [a, a] - Adds a to its own neighbor list; the nei not in visited check prevents infinite recursion, but the self-loop is an extra edge, usually caught by the n-1 count or making it non-tree.

        # Duplicate edges - Two [a,b] edges inflate the edge count past n-1 → caught by Line 1.







