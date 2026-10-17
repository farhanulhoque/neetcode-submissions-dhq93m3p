class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algorithm
        
        # Adjacency list: adj[u] = list of (neighbor, travel_time) edges from u
        adj = defaultdict(list)
        # For each edge (u, v, t), record that u reaches v with travel time t
        for u, v, t in times:
            adj[u].append((v, t))
        
        # The min-heap, seeded with (0, k) — source node k is reached at time 0
        minHeap = [(0, k)]
        # Visited set — nodes whose shortest time is finalized
        visited = set()
        # Tracks the maximum shortest-time seen (the answer: when the last node is reached)
        maxTime = 0

        # Dijkstra’s main loop: process until the heap empties
        while minHeap:
            # Pop the closest unvisited node (smallest time — the greedy choice)
            time, node = heapq.heappop(minHeap)
            # If this node is already finalized, skip it (this is a longer, outdated path to it)
            if node in visited:
                continue
            # Finalize this node — its time is now its shortest time
            visited.add(node)
            # Update the max (the latest-arriving node determines “all received”)
            maxTime = max(maxTime, time)

            # for each neighbor, if not yet finalized push it with the distance through this node (time + weight)
            for nei, weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time + weight, nei))
        
        # If all n nodes were reached, return the max time; else some node is unreachable → -1
        return maxTime if len(visited) == n else -1
        

        # TC: O(E · log V) -> building the adjacency list: O(E). The main loop: each edge, when relaxed, pushes at most once onto the heap → up to O(E) pushes. Each heap push/pop is O(log(heap size)) = O(log E) ≈ O(log V) (since E ≤ V²  → log E ≤ 2 log V). EEach node is finalized once; each edge is relaxed at most once. O(E · log V) overall — standard Dijkstra bound with a binary heap.
        # SC: O(V + E) -> adjacency list: O(V + E). The heap can hold up to O(E) entries (a node pushed per incoming relaxed edge) → O(E). Visited set: O(V). O(V + E) overall.

        # V = n (nodes), E = number of edges (len(times)).


        # Solution Description: The signal spreads from node k along weighted edges. The time for a node to receive the signal is the shortest path from k to it. The time for all nodes to receive it is when the last (farthest) node does — i.e., the maximum of all the shortest-path distances. So we run Dijkstra from k to find the shortest time to every node, then return the maximum of those times. If any node is unreachable (never finalized), the signal can’t reach everyone → return -1.


        # ----- Deep Dive -----

        # Dijkstra's Algorithm:

                # 1. A MIN-HEAP of (distance_from_source, node):
                #     → always pops the closest unvisited node. The greedy engine.

                # 2. A VISITED set (or finalized-distance map):
                #     → once a node is popped (finalized), its shortest distance is locked. We
                #     skip it if it comes up again. (A node can be pushed multiple times with
                #     different distances; we only process it the FIRST time it's popped —
                #     which is its shortest.)

                # 3. EDGE RELAXATION (the neighbor update):
                #     → for each neighbor, "relax" the edge: newDist = currentDist + edgeWeight.
                #     If newDist improves on the neighbor's best known distance, push it.
                #     "Relaxing" = trying to shorten a neighbor's distance via the current node.

                # The loop:
                #     pop the closest node (heap).
                #     if already finalized (visited), skip it.
                #     finalize it (record its distance, mark visited).
                #     relax all its edges (push improved neighbor distances onto the heap).
                #     repeat until the heap empties (or all nodes finalized).

                # BFS world (unweighted): every hop costs 1 → fewest hops = shortest.
                # Dijkstra world (weighted): edges cost different amounts → we need shortest
                #                         TOTAL weight, not fewest edges.
                #     A --1--> B --1--> C   (total 2)
                #     A --5--------> C       (total 5)
                #     BFS would say A→C is "1 hop" (shortest). But A→B→C (cost 2) is actually
                #     shorter in TOTAL TIME than A→C (cost 5). BFS can't handle this. Dijkstra can.

                # The greedy principle:
                #     "Among all nodes I haven't finalized yet, process the CLOSEST one next."
                # Why closest-first? Because once you've found the shortest way to the closest
                # unvisited node, NOTHING can make it shorter later — any other path to it would
                # have to go through a FARTHER node first, which is already longer. So the
                # closest node's distance is FINAL the moment we reach it.
                # This is the greedy insight: the nearest unvisited node's shortest distance is
                # locked in — we can safely finalize it and move on.

                # Dijkstra cannot handle negative weights — negatives break the greedy “closest is final” invariant. 
        

        # Why the answer is the MAX of shortest distances -> Dijkstra gives the SHORTEST time for the signal to reach each node individually. But the question asks when ALL nodes have received it. All nodes have the signal once the SLOWEST-to-receive node gets it. That's the MAXIMUM of all the shortest-path times.
                # node A receives at time 1, B at time 3, C at time 4.
                # → "all received" happens at time 4 (when C, the last one, gets it).
                # → answer = max(1, 3, 4) = 4

                # We track maxTime as we finalize each node (each pop gives a node's shortest time, in increasing order — so the LAST finalized node's time is the max).
        

        # Why (time + weight, nei) — relaxation, and why time goes first in the tuple -> RELAXATION: the time to reach neighbor `nei` THROUGH the current node is (current node's time) + (edge weight) = time + weight. We push (time + weight, nei) — the candidate distance to nei via this path. The heap will later pop the SMALLEST such candidate for nei first (its shortest). WHY TIME FIRST in the tuple: Python heaps compare tuples left-to-right. Putting `time` first makes the heap order by TIME (distance) — exactly what Dijkstra's "closest first" needs. If node came first, it'd order by node label (wrong). (time + weight, nei): the heap ranks by the accumulated time → pops the closest-reached node next → greedy correctness.

        # Why the visited check is essential -> A node can be pushed onto the heap MULTIPLE times — reached via different paths with different total times. The heap pops the SMALLEST-time version first. When we pop a node the FIRST time, it's via its shortest path → finalize it (add to visited, record its time). Any LATER pop of the same node has a larger time (a worse path) → "if node in visited: continue" skips it.

        # Without this check: we'd re-process nodes via longer paths → wrong distances and wasted work. The check ensures each node is finalized EXACTLY ONCE, at its shortest time. This is the heart of Dijkstra's correctness (from the concept section).

        # Why seeding (0, k) and why len(visited) == n detects unreachability -> 
                # SEEDING (0, k): the signal STARTS at node k at time 0 (it's already there).
                # So Dijkstra begins from k with distance 0, spreading outward.

                # UNREACHABILITY: if some node can't be reached from k (no path), Dijkstra never
                # finalizes it → it's never added to visited. So len(visited) < n means some
                # node never got the signal → impossible → return -1.

                # len(visited) == n → all n nodes reached → return the max time.
                # len(visited) < n  → some node unreachable → return -1.

                # This is how we detect the "-1" case: count how many nodes Dijkstra actually finalized.


        # ----- Edge Cases -----

        # Single node (n=1, source k) -> Heap seeds (0, k), finalizes k at time 0, len(visited)=1==n → returns 0 (the lone node has the signal instantly).

        # Unreachable node -> Never finalized → len(visited) < n → returns -1.

        # Disconnected graph -> Nodes in k’s reachable component get finalized; others don’t → len(visited) < n → -1.

        # Zero-weight edges (t=0) -> Allowed (problem says t ≥ 0); relaxation time + 0 works fine — a neighbor reached instantly. Dijkstra handles non-negative weights including 0.

        # Self-loop or parallel edges -> Harmless — a self-loop pushes the node again (skipped if visited); parallel edges push multiple candidates (heap picks the smallest).

        # All nodes reachable in one hop -> Each neighbor finalized at its edge weight; max of those is the answer.

        # Source has no outgoing edges (n > 1) -> Only k is finalized → len(visited)=1 < n → -1.







