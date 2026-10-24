class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST (Minimum Spanning Tree) & PRIM’S ALGORITHM

        # n = number of points
        n = len(points)
        # visited = points already in the MST (the growing tree)
        visited = set()
        # Min-heap seeded with (0, 0) — start at point 0 with cost 0 (the first node is free)
        minHeap = [(0, 0)]
        # Running total of edge costs = the MST weight
        totalCost = 0
        
        # Keep going until all n points are in the tree
        while len(visited) < n:
            # Pop the cheapest frontier edge — (cost, point_index)
            cost, i = heapq.heappop(minHeap)
            # If this point is already in the tree, skip it (a more expensive, outdated edge to it)
            if i in visited:
                continue
            # Add this point to the tree
            visited.add(i)
            # Add its edge cost to the total (connecting it to the tree)
            totalCost += cost

            # Get this point’s coordinates
            xi, yi = points[i]
            # Consider edges to every other point (complete graph), but only points not yet in the tree (not visited)
            for j in range(n):
                if j not in visited:
                    # Get the other point’s coordinates
                    xj, yj = points[j]
                    # Compute the Manhattan distance (the edge weight)
                    dist = abs(xi - xj) + abs(yi - yj)
                    # Push this candidate edge (dist, j) onto the heap
                    heapq.heappush(minHeap, (dist, j))
        
        # All points connected → return the total MST cost
        return totalCost


        # TC: 
        # SC: 
        

        # Solution Description: “Connect all points, one path between each pair, minimum cost” is a minimum spanning tree. Every pair of points can be connected (the graph is complete), with each edge’s weight being the Manhattan distance between the two points. We run Prim’s: start from point 0, and greedily grow the tree by repeatedly adding the cheapest edge connecting the current tree to a point not yet in it. A min-heap surfaces the cheapest frontier edge. Each time we add a new point, we add its edge cost to the running total. When all points are connected, the total is the minimum cost. Since the graph is complete, from each newly-added point we consider edges (Manhattan distances) to all not-yet-added points.


        # ----- Deep Dive -----

        # MST & PRIM’S ALGORITHM: 

            # The Three Pieces of Prim’s:

                # 1. A MIN-HEAP of (edge_cost, node):
                # → pops the cheapest edge to a node not yet in the tree.

                # 2. A VISITED set (nodes already in the tree):
                # → once a node is added, skip any later (more expensive) edges to it.
                #     A node can be pushed multiple times with different edge costs; we take it
                #     via its CHEAPEST edge (the first time it's popped).

                # 3. A RUNNING TOTAL of edge costs:
                # → sum the cost each time we add a new node to the tree. That's the MST weight.

                # The loop:
                #     pop the cheapest frontier edge (heap).
                #     if its node is already in the tree, skip.
                #     add the node (add its cost to the total), mark visited.
                #     push all its edges to not-yet-added nodes.
                #     repeat until all n nodes are in the tree.
            
            # Prim’s vs Dijkstra: The One Crucial Difference:
                
                # DIJKSTRA's heap key = TOTAL distance from the SOURCE to a node.
                #     (accumulated path cost: time_so_far + edge_weight)

                # PRIM's heap key = the cost of a SINGLE edge connecting a node to the tree.
                #     (just the edge weight itself — NOT accumulated)

                # Why the difference?
                #     Dijkstra wants shortest PATHS from a source → it accumulates path costs.
                #     Prim's wants the cheapest TREE → it only cares about each individual edge's
                #     cost to attach a new node, not the path back to any source.

                #     Dijkstra: push (dist_so_far + weight, neighbor)   ← accumulated
                #     Prim's:   push (weight, neighbor)                 ← just the edge weight

                # That's the ONLY real difference in the code. Same heap, same visited-skip, same
                # greedy loop — but Prim's doesn't add the current cost to the edge weight.
        

        # Why push (dist, j) — just the edge weight (the Prim’s key) -> We push (dist, j) where dist is JUST the Manhattan distance from point i to point j — the cost of that ONE edge connecting j to the tree. We do NOT add totalCost or any accumulated value (that would be Dijkstra). Why? Prim's minimizes the TOTAL TREE weight by always adding the cheapest individual edge to a new node. The cost to attach j is just the edge i—j, not a path from any source. So the heap key is the raw edge weight. Dijkstra here would wrongly push (totalCost + dist, j) → that's path cost from the start, not edge cost → would build a shortest-path tree, NOT an MST. Pushing just `dist` is THE thing that makes this Prim's (MST) rather than Dijkstra (shortest paths).

        # Why seed (0, 0) and the first node is “free” -> 


        # ----- Edge Cases -----


        