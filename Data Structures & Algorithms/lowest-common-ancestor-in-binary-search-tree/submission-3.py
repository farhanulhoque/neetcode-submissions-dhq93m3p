# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Iterative (Directional walk)

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



        # Solution Description: In a BST, every node splits values: everything smaller goes left, everything larger goes right. So the LCA of p and q is the first node where p and q would go in different directions (one left, one right) — or where the node is p or q. We walk down from the root: if both p and q are smaller than the current node, the LCA must be to the left. If both are larger, it's to the right. Otherwise — they split here (one smaller/equal, one larger/equal, or one is this node) — this node is the LCA. Because we only ever go one direction, this is O(h), much faster than searching the whole tree.


        # ----- Deep Dive -----

        # 






