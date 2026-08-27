# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # In-order Traversal (Recursion)

        # This is to track the previously visited value (starts at -∞). A list so the nested function can mutate it
        prev = [float("-inf")]

        # In-order helper: left → node → right
        def inorder(node):
            # Base case: empty node is valid
            if not node:
                return True
            
            # Recurse left first — if the left subtree is invalid, bail
            if not inorder(node.left):
                return False
            
            # The current value must be strictly greater than the previous — else not increasing → invalid
            if node.val <= prev[0]:
                return False
            
            # Update prev to the current value
            prev[0] = node.val
            
            # Recurse right
            return inorder(node.right)
        
        # Kick off the traversal
        return inorder(root)


        # TC: O(n) -> In-order visits every node once; short-circuits on the first violation
        # SC: O(h) -> Recursion call stack depth = tree height h


        # Solution Description: This exploits a beautiful BST property: an in-order traversal of a BST visits values in strictly increasing order. So we do an in-order traversal (left → node → right) and check that each value is strictly greater than the previous one. If any value isn't, it's not a valid BST. This is often considered the cleanest BST-validation approach.


        # ----- Deep Dive -----

        # Why in-order traversal of a BST is sorted -> In-order traversal (left → node → right) of a valid BST produces strictly increasing values — because left (smaller) is visited before the node, which is visited before right (larger). So validating a BST reduces to checking that the in-order sequence is strictly increasing. This is one of the most important BST properties.

        # Why we track prev and check "<=" -> We track prev (the last in-order value) and require node.val > prev — checking node.val <= prev catches both decreases and duplicates (the == case). Strictly increasing is the exact BST condition. prev = -∞ initially lets the first node always pass.

        # Why the recursion order (left, check, right) matters -> The strict left → node → right order is essential — it's what produces the sorted sequence. Checking the node before fully traversing its left subtree would compare values out of order, breaking the prev comparison. The order is the algorithm.






