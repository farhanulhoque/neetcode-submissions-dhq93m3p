class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        minHeap = [(0, k)]
        visited = set()
        maxTime = 0

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
        

        # TC:
        # SC:


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


        # ----- Edge Cases -----

        # 







