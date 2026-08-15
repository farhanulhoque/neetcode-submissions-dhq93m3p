# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Iterative DFS

        # Empty tree is balanced
        if not root:
            return True
        
        # This is to Map node → its height
        heights = {}
        # Stack of (node, visited) — the flag enables postorder
        stack = [(root, False)]
        
        # Process until the stack empties
        while stack:
            # Pop a node and its flag
            node, visited = stack.pop()
            # If visited, both children are done → process this node
            if visited:
                # Get left and right children's heights (0 if None)
                leftHeight = heights.get(node.left, 0)
                rightHeight = heights.get(node.right, 0)
                # Balance check → return False immediately on violation
                if abs(leftHeight - rightHeight) > 1:
                    return False
                # Store this node's height
                heights[node] = 1 + max(leftHeight, rightHeight)
            # First encounter (visited False)
            else:
                # Re-push as visited=True — processed after children
                stack.append((node, True))
                # Push children (unvisited) — processed before the re-pushed parent
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
        # No violation → balanced
        return True


        # TC: O(n) -> Each node pushed/popped twice → O(2n) = O(n); can stop early on imbalance
        # SC: O(n) -> Stack holds up to O(h), but the heights map stores all n nodes → O(n) overall
        # Matches DFS's time; uses O(n) space for the heights map (recursion avoided this via return values).


        # Solution Description: Replaces recursion with an explicit stack while preserving postorder via the visited-flag trick (same as Diameter's iterative version). We process each node only after its children, computing heights into a map and checking balance. If any node is unbalanced, we can return False immediately.


        # ----- Deep Dive -----

        # The visited flag for postorder -> Balance check needs children's heights first → postorder needed. A plain stack processes a node when first popped (too early). The visited flag defers the parent: 1st pop (False): "not ready — push children, re-push myself as True", 2nd pop (True):  "children done — NOW check my balance".

        # iterative DFS processes nodes as it goes and can return False the moment it finds imbalance. This is closer to recursive DFS's early termination — though it still doesn't have the elegant -1 propagation, it does stop the traversal early on the first violation.






