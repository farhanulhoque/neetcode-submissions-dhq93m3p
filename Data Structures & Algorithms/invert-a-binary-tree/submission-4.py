# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the node is None (empty), there's nothing to invert. Return None — an empty tree inverts to an empty tree
        if not root:
            return None
        
        # Swap this node's left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the (now-swapped) left subtree
        self.invertTree(root.left)
        # Recursively invert the (now-swapped) right subtree
        self.invertTree(root.right)

        # Return this node — the root of the inverted (sub)tree
        return root


        # TC: O(n) -> We visit every node exactly once, doing O(1) work (a swap) at each. n = number of nodes
        # SC: O(h) -> The recursion call stack goes as deep as the tree's height h. Balanced tree → O(log n); completely unbalanced (a "linked list" tree) → O(n) worst case

        # Solution Description: Inverting a tree means mirroring it — every node's left and right children swap places, all the way down. The elegant insight: to invert a tree, swap the root's two children, then invert each subtree the same way. That self-similar structure ("solve the whole by solving the parts identically") is exactly what recursion expresses. We recurse down to the leaves, swapping children at every node. The base case is an empty node (None), where there's nothing to swap.


        # ----- Deep Dive -----

        # Understanding the O(h) space: each recursive call adds a frame to the call stack, and the deepest chain of active calls equals the tree's height. A balanced tree of n nodes has height log n, so O(log n) space. A degenerate tree (every node has one child) has height n, so O(n). This "space = height" rule holds for almost all recursive tree solutions.

        # The base case — why if not root: return None -> Every recursion needs a stopping point, or it recurses forever. The tree is finite — eventually the recursion walks off the bottom, past the leaves, into "empty" (None) spots where children would be. When root is None, there's nothing to swap → just return.

        # How recursion actually works -> Don't trace every level in your head — trust that the recursive call does its job. To invert a tree, swap the two children, then TRUST that invertTree correctly inverts each subtree. You don't manually trace what happens 3 levels down. You assume invertTree works on smaller trees, and build on that. Each subtree is a SMALLER version of the same problem. You just need to (a) handle the base case, and (b) correctly combine the results of recursive calls.

        # Why order doesn't matter here (swap before or after recursion) -> the swap and the subtree inversions are independent operations, the order is flexible here. (This won't be true for all tree problems — some require processing children before or after the parent. But for inversion, either works.)






