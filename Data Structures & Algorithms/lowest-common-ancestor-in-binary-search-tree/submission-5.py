# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Iterative (Directional walk) - Optimal

        # Start at the root
        curr = root

        # Walk down until we find the split point
        while curr:
            # Both p and q are larger than the current node → LCA is in the right subtree. Move right.
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Both are smaller → LCA is in the left subtree. Move left.
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # They split here (one ≤ current, one ≥ current, or current is p or q) → this is the LCA
            else:
                return curr
        

        # TC: O(h) -> We walk down a single path from root toward the split point — at most the tree's height h. Balanced BST → O(log n); skewed → O(n). O(h) time (vs O(n) for a full tree search) is the payoff of exploiting the BST property: we only ever explore one path, discarding half the remaining tree at each step — exactly like binary search.
        # SC: O(1) -> Just one pointer curr — no recursion, no extra structures


        # Solution Description: In a BST, every node splits values: everything smaller goes left, everything larger goes right. So the LCA of p and q is the first node where p and q would go in different directions (one left, one right) — or where the node is p or q. We walk down from the root: if both p and q are smaller than the current node, the LCA must be to the left. If both are larger, it's to the right. Otherwise — they split here (one smaller/equal, one larger/equal, or one is this node) — this node is the LCA. Because we only ever go one direction, this is O(h), much faster than searching the whole tree.


        # ----- Deep Dive -----

        # Why the split point IS the LCA -> The LCA is the split point because that's the deepest node where p and q still share a subtree. Above it, both are descendants; below it, they diverge into different subtrees. The BST ordering lets us detect this split with a single value comparison.

        # Why the else handles "a node IS p or q" -> The else branch fires when the current node is p or q (value equal), correctly returning it as the LCA. This handles "a node can be its own ancestor" — if p is an ancestor of q, the walk reaches p, the strict >/< checks both fail, and else returns p.

        # Why no explicit p/q found check is needed -> Because the problem guarantees p and q are in the tree, the split point always exists and else always fires before curr hits None. No "not found" handling is needed — the while curr is a safety formality that never actually exhausts. If p or q might not exist, we'd need to handle curr becoming None, but the problem's guarantee lets us keep it simple.






