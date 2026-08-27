# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS

        # Helper carrying the valid range (low, high) for this node
        def valid(node, low, high):
            # Base case: empty node is trivially a valid BST
            if not node:
                return True
            
            # The node must be strictly within (low, high) — else invalid
            if not low < node.val < high:
                return False
            
            # Left subtree: same low, but high tightens to node.val (left must be < node). Right subtree: low tightens to node.val (right must be > node), same high.
            return (valid(node.left, low, node.val) and valid(node.right, node.val, high))
        
        # Start with the widest range (-∞, +∞) — the root can be any value
        return valid(root, float("-inf"), float("inf"))


        # TC: O(n) -> Every node visited once, O(1) range check each. Short-circuits early on the first violation
        # SC: O(h) -> Recursion call stack depth = tree height h. Balanced → O(log n); skewed → O(n)
        # The (low, high) range travels on the call stack as parameters, no extra space beyond the recursion.


        # Solution Description: Recurse carrying a valid range (low, high) for the current node. A node is valid only if low < node.val < high. Going left, tighten high to node.val (left descendants must all be smaller). Going right, tighten low to node.val. The whole tree is a valid BST if every node satisfies its range.


        # ----- Deep Dive -----

        # Why the naive "check parent vs child" approach FAILS -> The naive approach checks each node against its DIRECT children only — but the BST property requires the ENTIRE subtree to satisfy the ordering.

        # How the range enforces the FULL subtree constraint -> The (low, high) range is what captures all ancestor constraints, not just the parent. The range ACCUMULATES constraints from ALL ancestors as we descend. How bounds tighten going down: go LEFT  → high = node.val (everything left must be < this node), go RIGHT → low  = node.val   (everything right must be > this node). Each ancestor contributes a bound; the range carries them ALL down.

        # Why strict inequality "low < node.val < high" -> Strict inequalities (<, not <=) enforce the "strictly less / strictly greater" rule — duplicates aren't allowed in this BST definition. A child equal to an ancestor bound fails the strict check, correctly rejecting it. 

        # Why -∞ and +∞ for the root -> The root has NO ancestors → no constraints → it can be ANY value. We represent "no lower bound" as -inf and "no upper bound" as +inf: -inf < root.val < +inf (always true for any real value). As we descend, these infinite bounds get replaced by real ancestor values.






