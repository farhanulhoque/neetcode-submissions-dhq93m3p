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
            
            xi, yi = points[i]
            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(minHeap, (dist, j))
        
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
        

        # 


        # ----- Edge Cases -----


        