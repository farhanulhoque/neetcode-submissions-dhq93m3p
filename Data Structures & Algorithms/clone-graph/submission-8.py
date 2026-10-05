"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS

        # Guard: if the input node is null, return null (empty graph)
        if not node:
            return None

        # Hashmap to map each original node to its clone
        oldToNew = {}

        # DFS helper that returns the clone of cur
        def dfs(cur):
            # If this node is already cloned (in the map), return the existing clone (this is what stops cycles)
            if cur in oldToNew:
                return oldToNew[cur]

            # Otherwise, create a new clone with the same value
            copy = Node(cur.val)
            # Store the clone in the map before recursing (critical for cycles)
            oldToNew[cur] = copy

            # Loop over the original node's neighbors. 
            for nei in cur.neighbors:
                # Recursively clone each neighbor and append the clone to this copy's neighbor list
                copy.neighbors.append(dfs(nei))

            # Return the fully-wired clone
            return copy

        # Kick off the clone from the given node
        return dfs(node) 


        # TC: O(V + E) -> each node is cloned exactly once (the map ensures this) → O(V) node creations. We traverse every neighbor link once across all nodes → O(E) edge processing. (each edge is examined from both endpoints in an undirected graph, but that's still O(E) total — a constant factor.)
        # SC: O(V) -> the hashmap holds one entry per node → O(V). The recursion stack can go O(V) deep (a long chain of nodes) → O(V).
 
        # Variables: V = vertices (nodes), E = edges.


        # Solution Description: Recursively clone from the given node. A hashmap maps each original node to its clone. For a node: if it's already in the map, return its existing clone (stops cycles). Otherwise, create its clone, store it in the map before recursing, then recursively clone each neighbor and attach them to the clone's neighbor list.


        # ----- Deep Dive -----

        # Why the hashmap is essential — handling cycles -> Undirected graph: if A connects to B, then B connects back to A (cycle). Naive clone (no map): clone A → clone A's neighbor B → clone B's neighbor A → clone A AGAIN → clone that A's neighbor B again → ... infinite loop. The map breaks this: once A is cloned and stored, the next time we reach A (coming back from B), we find it in the map and RETURN the existing clone instead of cloning again. clone A (store in map) → clone B (store) → B's neighbor A? → A IS in map → return A's clone → DONE, no infinite loop. The map serves TWO purposes: 1. stops infinite recursion on cycles, 2. ensures each original maps to ONE clone (shared neighbors share a copy).

        # Why store the clone BEFORE recursing (the ordering is critical) -> Why store before recursing? Because a neighbor might point BACK to cur (cycle), and when it does, dfs(cur) must find cur ALREADY in the map. If we recursed FIRST and stored AFTER: clone A → recurse to B → B recurses back to A → A NOT in map yet (we haven't stored it!) → clone A again → infinite loop. Storing BEFORE recursing means cur's clone exists in the map the moment we descend into neighbors. So any neighbor that loops back to cur finds it. create A's clone → store A→clone → NOW recurse into B → B loops back to A → A found in map → return A's clone → no loop.

        # Why copy.neighbors.append(dfs(nei)) wires copies to copies -> A deep copy must have its neighbor lists point to CLONES, not originals. For each original neighbor `nei`, dfs(nei) returns nei's CLONE (creating it if needed, or fetching it from the map). We append that CLONE to copy's neighbor list. 
            # original A.neighbors = [B, C]  (original B, original C)
            # clone A.neighbors    = [clone of B, clone of C]  ← copies, not originals
            # This recursively ensures the ENTIRE copied graph references only clones — a true deep copy with the same structure but all-new nodes.







