# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Iterative DFS

        # Empty tree → 0
        if not root:
            return 0
        
        # Running count of good nodes
        count = 0
        # Stack of (node, maxSoFar) — seed with root and its value
        stack = [(root, root.val)]

        # Process until the stack empties 
        while stack:
            # Pop a node and its path-max (LIFO)
            node, maxSoFar = stack.pop()

            # Good if node.val >= maxSoFar → increment
            if node.val >= maxSoFar:
                count += 1
            
            # Compute updated max for children
            maxSoFar = max(maxSoFar, node.val)
            
            # Push children with the updated max
            if node.left:
                stack.append((node.left, maxSoFar))
            if node.right:
                stack.append((node.right, maxSoFar))
        
        # Return the total number of good nodes
        return count


        # TC: O(n) -> Each node pushed and popped once
        # SC: O(n) -> The stack holds up to O(h) nodes along a path (depth-first)


        # Solution Description: The DFS logic with an explicit stack. We push (node, maxSoFar) tuples — same bundling as BFS, but a stack (LIFO) instead of a queue (FIFO). Pop a node with its path-max, check if it's good, and push children with the updated max. No visited flag is needed — this isn't postorder (a node's good-ness doesn't depend on its children's results).


        # ----- Deep Dive -----

        # Only the container differs from BFS -> The iterative DFS and BFS versions differ only in the container (stack vs queue). Since maxSoFar is bundled per-node in the tuple, traversal order is irrelevant to correctness — both count the same good nodes. This confirms Good Nodes is order-independent.

        # Why no visited flag (not postorder) -> No visited flag is needed because Good Nodes isn't postorder — a node's good-ness depends on ancestors (available immediately via the carried max), not on children's results. We decide as we visit, so a plain stack works.






