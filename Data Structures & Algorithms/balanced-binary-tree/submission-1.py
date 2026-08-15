# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS (Optimal)
        
        # This helper returns height — or -1 if unbalanced
        def dfs(node):
            # Base case: empty node has height 0 (and is trivially balanced)
            if not node:
                return 0
            
            # Get left and right subtree's height (or -1 if it's unbalanced)
            leftHeight = dfs(node.left)
            rightHeight =  dfs(node.right)

            # Unbalanced if: either child already returned -1, or the heights differ by more than 1 here
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                # Propagate the -1 sentinel upward — imbalance found
                return -1
            
            # Balanced so far → return the real height for the parent
            return 1 + max(leftHeight, rightHeight)

        # The tree is balanced iff the root's call isn't -1
        return dfs(root) != -1


        # TC: O(n) -> Each node visited once, O(1) work per node. The -1 short-circuit can make it faster in practice (stops early), but worst case is still O(n)
        # SC: O(h) -> Recursion call stack depth = tree height h. Balanced → O(log n); skewed → O(n)


        # Solution Description:


        # ----- Deep Dive -----

        # -1 isn't a default; it's explicitly returned by the return -1 line when a subtree fails the balance check. That -1 is born at the node where imbalance (abs(leftHeight - rightHeight) > 1) is first detected, then received by each ancestor's left/right variable as it propagates up to the root. So left = dfs(node.left) gives you -1 precisely when the entire left subtree below has already failed somewhere — the failure signal is just passing through.



            

        
