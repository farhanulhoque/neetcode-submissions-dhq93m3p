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

        # Return the deepest depth reached
        return result

        # TC: O(n) -> Each real node is pushed and popped once; None placeholders add at most O(n) more pops — still linear
        # SC: O(h) -> The stack holds at most one root-to-leaf path's worth of nodes at a time (plus their unpopped siblings) — proportional to the tree's height h
        

        # Solution Description: This mimics recursive DFS but manages the stack manually, avoiding recursion-depth limits. We pair each node with its depth in the stack. Popping a node, we update the running maximum with its depth and push its children carrying depth + 1. When the stack empties, we've seen every node's depth and kept the largest.


        # ----- Deep Dive -----

        # Why pair each node WITH its depth in the stack -> An explicit stack has no call frames, so depth must be tracked MANUALLY. We bundle it with each node. When we push children, we increment: (child, depth + 1) → each node carries its own depth, exactly like the recursion did. Without pairing, we'd have no way to know how deep a popped node is. The tuple replaces what the recursion's call stack tracked for free.

        # Why check if node AFTER popping (not before pushing) -> Pushing unconditionally and filtering None on pop keeps the code uniform. The None entries are harmless — they're popped and skipped. (You could check before pushing instead; both work.)

        # Why this gives the same answer despite different visit order -> Iterative DFS with a stack visits nodes in a DIFFERENT order than recursion (because we push left then right, but pop right first — LIFO). But depth is order-INDEPENDENT: we're taking the MAX over all nodes' depths. No matter what order we visit them, max(all depths) is the same.

        # Why do we use a stack -> A stack (LIFO) naturally produces depth-first order. Depth-first means: dive as deep as possible down one path before backtracking to try other paths. The key: whatever you push last, you process next. So after visiting a node and pushing its children, you immediately dive into a child — not back to a sibling. That's depth-first. Here's the deeper connection: recursion already uses a stack — the "call stack." When you write recursive DFS, the computer manages a stack of function calls behind the scenes. When we write ITERATIVE DFS with an explicit stack, we're just MANUALLY doing what recursion did automatically.

        # Like recursive DFS, the iterative version's space tracks height, not width — because the stack mirrors the recursion's call-stack behavior. The advantage over recursion: no risk of hitting Python's recursion-depth limit on extremely deep trees (~1000 frames), since the stack lives on the heap.




