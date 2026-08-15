# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS

        # Both nodes empty → they match (two empty trees are equivalent)
        if not p and not q:
            return True
        
        # Exactly one is empty (the other isn't) → structure differs → not equal
        if not p or not q:
            return False

        # Both exist but values differ → not equal
        if p.val != q.val:
            return False
        
        # Values match → recurse: both left subtrees must match and both right subtrees must match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


        # TC: O(n) -> We compare nodes in lockstep and stop at the first mismatch or when either tree ends. In the worst case (identical trees) it's O(n) where n is the node count.
        # SC: O(h) -> Recursion call stack depth = the height we descend to


        # Solution Description: Recurse on both trees simultaneously. At each pair of nodes: if both are empty, they match; if only one is empty or their values differ, they don't. Otherwise, the trees match here only if both the left subtrees match and the right subtrees match — recurse into both.


        # ----- Deep Dive -----

        # 





        
