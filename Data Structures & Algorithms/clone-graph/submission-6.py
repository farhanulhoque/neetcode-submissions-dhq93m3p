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


        # TC: 
        # SC: 


        # Solution Description: Recursively clone from the given node. A hashmap maps each original node to its clone. For a node: if it's already in the map, return its existing clone (stops cycles). Otherwise, create its clone, store it in the map before recursing, then recursively clone each neighbor and attach them to the clone's neighbor list.


        # ----- Deep Dive -----

        # 






