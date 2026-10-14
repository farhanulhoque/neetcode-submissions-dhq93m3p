class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union-Find

        # parent[i] = the node i points up to. list(range(n)) makes every node point to itself — so each node is its own leader, i.e. its own group of one
        parent = list(range(n))
        # rank[i] = the size of the group led by i (starts at 1 — each group has one member). Used to decide which leader absorbs the other when merging
        rank = [1] * n
        # count = number of groups, starting at n (every node is its own group)
        count = n

        # find(node) = “who is this node’s leader?” — climb up to the top
        def find(node):
            # Keep climbing while node is not a leader (a leader points to itself, so node == parent[node])
            while node != parent[node]:
                # Path compression: re-point node's parent to its grandparent, flattening the chain so future climbs are shorter
                parent[node] = parent[parent[node]]
                # Move up one level (to node’s parent)
                node = parent[node]
            # We’ve reached a self-pointing node — that’s the leader — return it
            return node
        
        # union(a, b) = “merge a’s group and b’s group” — returns 1 if a merge happened, 0 if they were already together
        def union(a, b):
            # Find both nodes’ leaders
            pa, pb = find(a), find(b)
            # If they share the same leader, a and b are already in the same group
            if pa == pb:
                # so there’s nothing to merge → return 0 (no change to the count)
                return 0

            # Union by rank: check if pa’s group is smaller than pb’s
            if rank[pa] < rank[pb]:
                # if so, swap them so pa is always the bigger group’s leader
                pa, pb = pb, pa
            # Point the smaller group’s leader (pb) at the bigger leader (pa) — the two groups are now one, led by pa
            parent[pb] = pa
            # Update pa’s group size to include the newly-absorbed members
            rank[pa] += rank[pb]

            # Return 1 — a real merge happened (two groups became one)
            return 1
        
        # Process each edge (each is a “connect these two” instruction)
        for a, b in edges:
            # Subtract union’s result from count: 1 if a merge happened (one fewer group), 0 if redundant (count unchanged)
            count -= union(a, b)
        
        # Return the final number of groups
        return count


        # TC: O(V + E) -> initializing parent/rank: O(V). Each edge calls union, which does 2 finds + maybe a merge. With path compression + union by rank, each find/union is O(α(n)) ≈ O(1). → O(E · α(n)) ≈ O(E) for all edges. O(V + E) effectively. α(n) (inverse Ackermann) ≤ 4 for any realistic n.
        # SC: O(V) -> parent array: O(V), rank array: O(V). NO adjacency list needed — we process edges directly as unions.


        # Solution Description: Every node starts in its own group (its own leader), so there are n groups. Each edge says “these two nodes are connected,” so we merge their groups. Using the leader model: find each node’s leader; if they’re different leaders, point one at the other (merging two groups into one) and drop the group count by 1. If they already share a leader, the edge is redundant — no merge, count unchanged. After all edges, the number of remaining groups (leaders) is the answer.


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
        

        # Why parent = list(range(n)) means “everyone is their own leader” -> list(range(n)) produces [0, 1, 2, ..., n-1], so: parent[0] = 0, parent[1] = 1, parent[2] = 2, ... → every node points to ITSELF. In the leader model, a node that points to itself IS a leader. So every node starts as the leader of its own group of one. → n nodes, each its own leader → n separate groups → count = n. This represents "we haven't processed any edges yet, so nobody is connected." Each node is an island of one.

        # How find climbs to the leader -> The loop condition "node != parent[node]" means "node is not a leader yet":
                # if node points to itself (node == parent[node]), node IS the leader → stop.
                # if node points elsewhere (node != parent[node]), keep climbing.

                # Walking up the chain:
                    # parent = [0, 0, 1]   (0 is leader; 1 points to 0; 2 points to 1)
                    # find(2):
                    #     p = parent[2] = 1
                    #     is 1 != parent[1]=0? YES (1 is not a leader) → climb: p = 0
                    #     is 0 != parent[0]=0? NO (0 points to itself = leader) → stop
                    #     return 0

                    # So 2's leader is 0 — we climbed 2 → 1 → 0.

                # Why find is the heart of everything:
                    # "are a and b connected?" → find(a) == find(b)? (same leader = same group)
                    # every union starts by finding both leaders.
                    # So find is called constantly — which is why we optimize it (path compression).
        

        # Path compression (flattening the chain - "parent[node] = parent[parent[node]]"" ) -> As find climbs through node, it re-points node to its GRANDPARENT (the node two levels up) instead of its parent. This shortens the chain. Each find "cleans up" the path it walks, so next time those nodes are much closer to the leader → future finds are faster. Without this, repeated finds on a long chain would each be slow (O(chain length)). With it, the tree flattens over time toward near-direct pointers to the leader.


        # Union by rank (attaching smaller under bigger) -> When merging two groups, we must pick which leader becomes the overall leader. We attach the SMALLER group under the BIGGER group's leader.
                # Why? Attaching the smaller tree under the bigger one keeps the result SHALLOW:
                #     - the smaller group's members gain one level of depth (now under the big leader).
                #     - but there are FEWER of them, so less total "deepening."
                #     - attaching big-under-small would deepen MORE nodes → taller tree → slower finds.

                # rank[x] tracks each group's size so we know which is bigger. The swap ensures pa is the bigger one; then pb (smaller) gets attached under pa. Ex: rank[pa]=3, rank[pb]=1 → pa is bigger → parent[pb]=pa, rank[pa] becomes 4.
                # Combined with path compression, this keeps every tree nearly flat → find is nearly O(1). Together they give O(α(n)) per operation

        
        # Why "count -= union(a, b)" counts components -> Start: count = n (every node its own group/leader). Each edge calls union, which returns:
                # 1 → a real merge happened: two DIFFERENT groups became one → count drops by 1.
                # 0 → redundant: the two nodes already shared a leader → no merge → count unchanged.

                # So count -= union(...) subtracts exactly 1 for each merge, 0 otherwise. Before a merge: 2 groups (2 leaders), after a merge: 1 group (1 leader) → one fewer group → count -= 1. After all edges, count = n − (number of merges) = the number of groups left = the number of connected components.

                # n=5, edges=[[0,1],[1,2],[3,4]]
                #     count=5
                #     union(0,1): different leaders → merge → return 1 → count=4
                #     union(1,2): find(1)=0, find(2)=2, different → merge → return 1 → count=3
                #     union(3,4): different → merge → return 1 → count=2
                #     → 2 components
        

        # Why same-leader means “already connected” (pa == pb) -> If find(a) == find(b), then a and b climb to the SAME leader → they're already in the same group (connected through earlier edges). Connecting them again is REDUNDANT — it doesn't merge anything new (they're already one group). So union returns 0, and count stays the same. 



        # ----- Edge Cases -----

        # No edges -> No unions called; every node stays its own leader; count stays n. Returns n (all isolated).

        # Single node (n=1) -> count=1, no edges → returns 1. One group of one.

        # All connected (one component) -> Successive merges collapse everyone under one leader; count drops to 1.

        # Fully disconnected -> No merges → count = n.

        # Redundant edges / cycles -> Each hits pa == pb → returns 0 → count unaffected. The group structure is already fixed.

        # Self-loop [a, a] -> find(a) == find(a) → same leader → returns 0 → no change. A node is trivially in its own group.

        # Duplicate edges -> First merges; the duplicate finds the same leader → returns 0 → correct count.






