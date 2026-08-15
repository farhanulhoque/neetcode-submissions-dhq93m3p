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

        # -1 isn't a default; it's explicitly returned by the return -1 line when a subtree fails the balance check. That -1 is born at the node where imbalance (abs(leftHeight - rightHeight) > 1) is first detected, then received by each ancestor's left/right variable as it propagates up to the root. So left = dfs(node.left) gives you -1 precisely when the entire left subtree below has already failed somewhere — the failure signal is just passing through. A value flows up from wherever it's returned. 0 flows up from None leaves, positive heights flow up from balanced subtrees, and -1 flows up from the first unbalanced node. Your left/right variables are just catching whatever the recursive call below them decided to return.

        # Because valid heights are always ≥ 0, -1 is a safe "impossible value" to mean "unbalanced." We don't need a separate boolean flag OR a side variable. The single return value carries BOTH pieces of info: "am I balanced?" (is it -1 or not?), "what's my height?" (if not -1, the value itself)

        # Why we check left == -1 or right == -1 — propagating failure -> Once ANY node is unbalanced, the WHOLE tree is unbalanced. So a -1 from below must propagate ALL the way up to the root. Without checking children for -1, we might overwrite the failure signal with a real height and "forget" that a deeper node was unbalanced.

        # Early termination — why this short-circuits efficiently -> Once -1 appears, it fast-tracks up the tree — every ancestor sees the -1 and immediately returns -1 without computing anything. This early termination is why the -1 sentinel approach is efficient: it stops meaningful work the moment imbalance is detected.

        # Why postorder (children before parent) -> checking balance at a node needs its children's heights first, so this is postorder (bottom-up).



            

        
