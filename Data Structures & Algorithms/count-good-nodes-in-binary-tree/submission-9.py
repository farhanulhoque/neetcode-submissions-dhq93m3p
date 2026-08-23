# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS

        # Helper carrying maxSoFar — the max value on the path so far
        def dfs(node, maxSoFar):
            # Base case: empty node contributes 0 good nodes
            if not node:
                return 0
            
            # This node is good if it's ≥ the path max (count it as 1, else 0)
            good = 1 if node.val >= maxSoFar else 0

            # Update the running max for this node's children
            maxSoFar = max(node.val, maxSoFar)

            # Add good nodes from the left and right subtree (passing the updated max). We hand the max DOWN to the child.
            good += dfs(node.left, maxSoFar)
            good += dfs(node.right, maxSoFar)

            # Return the total good count for this subtree
            return good
        
        # Start at the root; initial max is root.val (the root is always good)
        return dfs(root, root.val)

        # TC: O(n) -> Every node visited once, O(1) work
        # SC: O(h) -> Recursion call stack depth = tree height h. Balanced → O(log n); skewed → O(n)
        # The maxSoFar parameter travels on the call stack, adding no extra space beyond the recursion itself.


        # Solution Description: Recurse down the tree carrying maxSoFar (the largest value on the path from the root to the current node). At each node: it's good if node.val >= maxSoFar. Update the max to max(maxSoFar, node.val) and pass it to both children. Sum up the good-node counts from both subtrees plus this node's own contribution.


        # ----- Deep Dive -----

        # Passing state DOWN -> "good" depends on ANCESTORS (the path above), not descendants. A node needs to know what came BEFORE it on the path. That info naturally flows from parent to child → downward parameter. The maxSoFar parameter carries state downward — each node passes the updated path-max to its children. This is the opposite of the "return info up" pattern.

        # Why >= and not > -> The definition forbids ancestors greater than the node — an ancestor equal to the node is fine. A node matching the path max has no ancestor strictly greater than it, so it's good.

        # Why the root is always good — initializing max to root.val -> The root has NO ancestors → no node above it can be greater → always good. Initializing maxSoFar = root.val makes the root automatically good (it equals the max, so >= holds) — no special case needed.

        # Why we sum (not max) the subtree results -> We sum the subtree results (not max) because we're counting all good nodes across the entire tree — every good node in every subtree contributes.






