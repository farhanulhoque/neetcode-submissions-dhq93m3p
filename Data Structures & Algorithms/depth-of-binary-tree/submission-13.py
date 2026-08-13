# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterativr DFS

        stack = [(root, 1)]
        result = 0

        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        
        return result

        # TC: O(n) -> Each real node is pushed and popped once; None placeholders add at most O(n) more pops — still linear
        # SC: O(h) -> The stack holds at most one root-to-leaf path's worth of nodes at a time (plus their unpopped siblings) — proportional to the tree's height h
        

        # Solution Description: This mimics recursive DFS but manages the stack manually, avoiding recursion-depth limits. We pair each node with its depth in the stack. Popping a node, we update the running maximum with its depth and push its children carrying depth + 1. When the stack empties, we've seen every node's depth and kept the largest.