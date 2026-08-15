# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS

        # Empty tree → 0
        if not root:
            return 0
        
        # Track the best diameter
        diameter = 0
        # This is to Map node → its height
        heights = {}
        # Stack of (node, visited) pairs — the visited flag enables postorder
        stack = [(root, False)]

        # Process until the stack empties
        while stack:
            # Pop a node and its flag
            node, visited = stack.pop()
            # If visited is True, both children are already done → process this node now
            if visited:
                # Look up children's heights (left and right) (0 if None)
                leftHeight = heights.get(node.left, 0)
                rightHeight = heights.get(node.right, 0)
                # Update the diameter with the path through this node
                diameter = max(diameter, leftHeight + rightHeight)
                # Store this node's height
                heights[node] = 1 + max(leftHeight, rightHeight)
            # First time seeing this node (visited is False)
            else:
                # Re-push it as visited=True — it'll be processed after its children
                stack.append((node, True))
                # Push children (as unvisited) — they'll be processed before the re-pushed parent
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
        # Return the best diameter
        return diameter


        # TC: O(n) -> Each node is pushed twice and popped twice — still O(2n) = O(n)
        # SC: O(n) -> The stack can hold up to O(h) for the path, but the heights map stores all n nodes → O(n) overall
        # The iterative version matches DFS's time but uses O(n) space for the heights map (recursion avoided this by passing heights via return values).

        # Solution Description: This replaces recursion with an explicit stack while preserving the crucial postorder (children-before-parent) processing. We use a stack and a heights map. The tricky part is achieving postorder iteratively — we process a node only after both its children have been visited, tracking heights in the map so each node can look up its children's heights when it's finally processed.


        # ----- Deep Dive -----

        # The visited flag trick -> we need to process a node AFTER its children (postorder), but a stack naturally processes a node when we first pop it (too early!). The flag converts a stack (which is naturally preorder-ish) into POSTORDER by deferring the parent until after its children. The visited flag makes each node get handled twice: first to schedule its children (and re-schedule itself behind them), then to actually process it once the children are done.

        # Why the parent is re-pushed BEFORE the children -> Stack is LIFO — last pushed is popped first. We push parent (True), THEN children (False). So children sit ON TOP of the parent in the stack → children get popped and processed BEFORE the parent's second pop. parent(True) waits at the bottom until children are done.



        
            