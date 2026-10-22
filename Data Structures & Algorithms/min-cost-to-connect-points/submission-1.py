class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST (Minimum Spanning Tree) & PRIM’S ALGORITHM

        n = len(points)
        visited = set()
        minHeap = [(0, 0)]
        totalCost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            totalCost += cost
            xi, yi = points[i]
            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(minHeap, (dist, j))
        
        return totalCost
        

        # Solution Description: 


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


        