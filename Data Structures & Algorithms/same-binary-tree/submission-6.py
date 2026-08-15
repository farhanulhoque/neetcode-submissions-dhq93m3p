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

        # The order of the three base checks — why it matters -> The order is "both-None → one-None → values". Check 1 (both None): handles the "both empty" case FIRST. After this passes, we know NOT both are None. Check 2 (one None): now, "not p or not q" catches "exactly one is None." Because check 1 already ruled out "both None," this OR specifically means "one is None, the other isn't" = structure mismatch. Check 3 (values): if we reach here, BOTH p and q exist (neither is None). So accessing p.val and q.val is SAFE — no null crash. Checking values first would crash on empty nodes.

        # Why and between the two recursive calls -> For two trees to be equivalent, EVERYTHING must match: the left subtrees must match  AND  the right subtrees must match. The and enforces that both subtrees must match — a difference anywhere makes the whole comparison False. Both trees are walked in the SAME order, position by position. Corresponding nodes are always compared against each other.





        
