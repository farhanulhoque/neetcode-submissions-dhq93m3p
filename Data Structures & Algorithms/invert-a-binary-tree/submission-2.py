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


        # TC: O(n) -> 
        # SC: O(n) -> 

        # Solution Description: Inverting a tree means mirroring it — every node's left and right children swap places, all the way down. The elegant insight: to invert a tree, swap the root's two children, then invert each subtree the same way. That self-similar structure ("solve the whole by solving the parts identically") is exactly what recursion expresses. We recurse down to the leaves, swapping children at every node. The base case is an empty node (None), where there's nothing to swap.


        # ----- Deep Dive -----

        # 