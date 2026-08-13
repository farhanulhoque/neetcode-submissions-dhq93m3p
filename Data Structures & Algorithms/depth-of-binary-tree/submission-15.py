# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS

        # Stack of (node, depth) pairs — start with root at depth 1
        stack = [(root, 1)]
        # Track the maximum depth seen
        result = 0

        # Process until the stack empties
        while stack:
            # Pop a (node, depth) pair (LIFO — last in, first out)
            node, depth = stack.pop()
            # Only process real nodes — skip None
            if node:
                # Update the max with this node's depth
                result = max(result, depth)
                # Push the left and right child with depth + 1
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        # 	Return the deepest depth reached
        return result

        # TC: O(n) -> Each real node is pushed and popped once; None placeholders add at most O(n) more pops — still linear
        # SC: O(h) -> The stack holds at most one root-to-leaf path's worth of nodes at a time (plus their unpopped siblings) — proportional to the tree's height h
        

        # Solution Description: This mimics recursive DFS but manages the stack manually, avoiding recursion-depth limits. We pair each node with its depth in the stack. Popping a node, we update the running maximum with its depth and push its children carrying depth + 1. When the stack empties, we've seen every node's depth and kept the largest.


        # ----- Deep Dive -----

        # 




