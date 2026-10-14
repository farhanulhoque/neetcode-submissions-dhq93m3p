class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find

        # n = number of edges (also the number of nodes, since there are n nodes labeled 1..n)
        n = len(edges)
        # parent[i] for nodes 1..n; n + 1 sized so index n is valid (nodes are 1-indexed, so index 0 is unused). Each node starts as its own leader
        parent = list(range(n + 1))
        # rank[i] = each group’s size, starting at 1
        rank = [1] * (n + 1)

        # find(node) = climb to the node’s leader
        def find(node):
            # Climb while node is not a leader (not self-pointing)
            while node != parent[node]:
                # Path compression: re-point node to its grandparent, flattening the chain
                parent[node] = parent[parent[node]]
                # Move up
                node = parent[node]
            # Return the leader (self-pointing node)
            return node
        
        # union(a, b) = merge the two groups; returns False if they’re already together
        def union(a, b):
            # Find both nodes’ leaders
            pa, pb = find(a), find(b)
            # If they share a leader, a and b are already connected. So this edge closes a cycle → return False (no merge)
            if pa == pb:
                return False
            
            # Union by rank: ensure pa is the larger group
            if rank[pa] < rank[pb]:
                # Swap so pa is the bigger leader
                pa, pb = pb, pa
            # Attach the smaller group (pb) under the bigger leader (pa)
            parent[pb] = pa
            # Update the combined group size
            rank[pa] += rank[pb]

            # Return True — a real merge happened
            return True
        
        # Process each edge in input order
        for a, b in edges:
            # If union fails (the two nodes already share a leader). This edge is the redundant one → return it
            if not union(a, b):
                return [a, b]

        
        # TC: O(V + O(E·α(n)) ≈ O(V) -> initializing parent/rank: O(n). Processing each edge: find + union, each O(α(n)) ≈ O(1) with path compression + union by rank → O(n · α(n)) ≈ O(n) for all edges. O(n) effectively (α(n) ≤ 4 is a tiny constant).
        # SC: O(V) -> parent and rank arrays, size n+1 → O(n). NO adjacency list needed — edges processed directly as unions → O(n).
        # α() is used for amortized complexity


        # Solution Description: We start with a tree (n-1 edges, no cycle) and add one extra edge, creating exactly one cycle. We must find and remove the edge that completes that cycle — and if the cycle could be broken at multiple edges, return the one appearing last in the input. Union-Find solves this directly. Process edges in input order, unioning each edge’s two nodes. For most edges, the two nodes are in different groups (different leaders) → they merge normally. But the redundant edge connects two nodes already in the same group (same leader) — meaning a path already exists between them, so this edge closes a cycle. That’s the edge to remove. Because we process in input order, the first edge that fails to union is exactly the last-appearing redundant edge the problem wants.


        # ----- Deep Dive -----

        # Why the redundant edge is the one that fails to union -> Process edges in order, unioning each. For a normal edge, its two nodes are in DIFFERENT groups (different leaders) → union merges them, returns True. The REDUNDANT edge is different: by the time we reach it, its two nodes are ALREADY in the same group (same leader), because earlier edges already built a path between them. 
                # find(a) == find(b) → a and b already connected → adding this edge creates
                # a SECOND path between them → a CYCLE.
                # So the edge that makes union return False is EXACTLY the edge that closes the cycle — the redundant one we must remove.

                # tree so far: 1—2—3 (all one group, led by 1)
                #     redundant edge [1,3]: find(1)=1, find(3)=1 → SAME leader → cycle 1-2-3-1!
                #     → union fails → [1,3] is the answer.
        

        # Why processing in input order gives the LAST-appearing answer -> The problem says: if multiple edges could be removed to fix the cycle, return the one appearing LAST in the input. Here's why processing in order and returning the FIRST failure gives exactly that:
                # A tree + 1 edge has EXACTLY ONE cycle. All edges on that cycle are "removable" candidates (removing any one breaks the cycle). As we process edges in order, we successfully union every edge UNTIL we hit the one that closes the cycle. That cycle-closing edge is, by definition, the LAST edge of the cycle to be processed (all the others came before it and were unioned successfully). → the first union-failure = the last cycle edge in input order = the answer. So "first failure while processing in order" automatically equals "last- appearing removable edge." No extra work needed.

                # edges = [[1,2],[2,3],[3,1]]  (cycle 1-2-3-1)
                #     [1,2]: union OK (merge {1}{2} → {1,2})
                #     [2,3]: union OK (merge {1,2}{3} → {1,2,3})
                #     [3,1]: find(3)=find(1) → SAME → FAIL → return [3,1]
                #     [3,1] is the last edge of the cycle in input order → correct answer
        

        # Why parent = list(range(n + 1)) — the 1-indexed adjustment -> The nodes are labeled 1..n (NOT 0..n-1). So we need valid parent/rank entries for indices 1 through n. 
                # list(range(n + 1)) = [0, 1, 2, ..., n] → indices 0 through n are valid. index 0 is unused (no node labeled 0), but it keeps the array big enough for index n.
                # If we used list(range(n)) (size n, indices 0..n-1), then accessing parent[n] (for the node labeled n) would be OUT OF BOUNDS.
                # The +1 accommodates the 1-indexed labeling. A tiny bit of wasted space (index 0), but it keeps the code clean — no need to subtract 1 from every node label.
        

        # Why there’s exactly one answer (no need to keep searching) -> The problem guarantees: start with a TREE (n-1 edges, no cycle), add EXACTLY ONE edge → exactly one cycle → exactly one redundant edge.
                # So the FIRST union-failure is the ONLY union-failure — we can return immediately without checking the rest.
                #     - all edges before the redundant one union successfully (building the tree).
                #     - the redundant edge fails (closes the cycle).
                #     - there are no edges after it that would also fail (only one extra edge
                #       was added, so only one cycle exists).

                # return on the first failure; no need to continue. The single guaranteed cycle makes this clean.

        # ----- Edge Cases -----

        # Minimum case (3 nodes, 3 edges — a triangle) -> [[1,2],[2,3],[3,1]]: first two union; [3,1] finds same leader → returned. The smallest possible input.

        # Redundant edge appears early vs late -> Regardless of position, the edge that closes the cycle (makes both endpoints already-connected) is the one caught — and it’s always the last cycle edge in input order.

        # Cycle via a long chain -> 1-2-3-4-5 then edge [5,1]: the chain unions successfully, [5,1] closes the cycle → returned. The leader climbing (with compression) handles the long chain efficiently.

        # Self-loop (not in this problem) -> The problem guarantees two different vertices, so no self-loops — but a self-loop [a,a] would trivially fail union (same leader) and be returned.

        # 1-indexed labels -> Handled by range(n+1) sizing; node n has a valid array slot.

        # The redundant edge connects two large subtrees’ shared ancestor -> find correctly climbs both endpoints to the same leader regardless of subtree size; union by rank kept the trees shallow.






        
