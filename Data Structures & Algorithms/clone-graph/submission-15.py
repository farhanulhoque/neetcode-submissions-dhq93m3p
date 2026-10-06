"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS

        # Guard: null input
        if not node:
            return None
        
        # Hashmap from original to clone
        oldToNew = {}
        # Clone the start node and store it (seed the map before the loop)
        oldToNew[node] = Node(node.val)
        # Queue seeded with the original start node
        q = deque([node])

        # Process until the queue empties
        while q:
            # Dequeue the next original node
            cur = q.popleft()
            # Loop over its neighbors. If the current neighbor hasn't been cloned yet, create its clone and store it. Enqueue the neighbor (so we process its neighbors later)
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                # Wire the current node's clone to the neighbor's clone
                oldToNew[cur].neighbors.append(oldToNew[nei])

        # Return the clone of the start node
        return oldToNew[node]


        # TC: O(V + E) -> each node is cloned once and enqueued/dequeued once → O(V). Each neighbor link is examined once to wire the edge → O(E).
        # SC: O(V) -> the hashmap holds one entry per node → O(V). The queue holds at most O(V) nodes → O(V).


        # Solution Description: Clone iteratively with a queue. First create the clone of the start node and map it. Then BFS: dequeue an original node, and for each of its neighbors, create the neighbor's clone if it doesn't exist yet (and enqueue it), then attach the neighbor's clone to the current node's clone. The map handles cycles exactly as in DFS.


        # ----- Deep Dive -----

        # Why we clone the start node BEFORE the loop -> We must put the start node's clone in the map BEFORE the BFS loop begins. Why? The loop processes a node by wiring its clone to its neighbors' clones (oldToNew[cur].neighbors...). For the very first node, oldToNew[cur] must already exist. So we seed the map with the start's clone up front. Then the loop can assume "cur's clone is always already in the map" (true for the start by seeding, and true for every other node because we clone it when first discovered as a neighbor). seed start's clone → loop maintains the invariant "cur is always cloned before we process it."

        # Why clone neighbors when DISCOVERED, and wire every edge -> Two separate actions, with different conditions:

            # CLONE + ENQUEUE (only if new): we create a neighbor's clone and enqueue it ONLY the first time we see it (if nei not in oldToNew). This clones each node once and processes each once — handles cycles.

            # WIRE THE EDGE (always): regardless of whether the neighbor is new, we ALWAYS append its clone to cur's clone neighbor list. Every edge must be wired, even to already-cloned nodes.

            # If we only wired edges to NEW neighbors, we'd miss edges to already-cloned nodes (like the back-edges in cycles) → incomplete copy. So: clone/enqueue once (inside the if), but wire the edge every iteration (outside the if).







