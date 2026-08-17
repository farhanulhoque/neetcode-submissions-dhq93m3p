# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # DFS 

        # Both p and q larger than the current node → LCA is right. Recurse into the right subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Both smaller → LCA is left. Recurse into the left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # They split here (or current is p/q) → this node is the LCA
        return root

        # TC: O(h) -> Walks one path down to the split — height h
        # SC: O(h) -> Recursion call stack depth = height h


        # Solution Description: The same directional logic, expressed recursively. If both p and q are greater than the current node, recurse right; if both smaller, recurse left; otherwise, this node is the LCA and we return it. Each recursive call moves one level down the single path toward the split.


        # ----- Deep Dive -----

        #  Why this recursion has NO explicit base case -> The problem GUARANTEES p and q are in the tree. So we're guaranteed to find the split point before running off the tree. The line "return root" acts as the "base case" — it's where recursion STOPS: once p and q don't both go the same direction, we return the node. We never recurse into None because the split ALWAYS happens at a real node.

        # Why it's tail recursion (and equivalent to the iterative version) -> Each call's last action is the recursive call itself, with nothing after. That makes it directly equivalent to the iterative loop (recurse right ≡ curr = curr.right). The recursion adds call-stack overhead but no extra logic.





