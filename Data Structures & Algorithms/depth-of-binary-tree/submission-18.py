# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS

        # Base case: an empty node has depth 0
        if not root:
            return 0
        
        # Recursively get the depth of the left and right subtree
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        # This node's depth = 1 (for itself) + the depth of the deeper child (longer path).
        return 1 + max(leftDepth, rightDepth)


        # TC: O(n) -> Every node is visited exactly once, doing O(1) work (a max and a +1) at each
        # SC: O(h) -> The recursion call stack goes as deep as the tree's height h. Balanced → O(log n); skewed (linked-list-like) → O(n) worst case.

        # Solution Description: The depth of a tree is 1 (for the current node) plus the depth of its deeper subtree. That self-similar definition is naturally recursive: the depth at any node is 1 + max(depth of left, depth of right), with an empty node having depth 0. That's the DFS approach. 


        # ----- Depp Dive -----

        # Why 1 + max(left, right) and not 1 + left + right -> Depth is the longest single path, so max picks the deeper subtree. Summing would count an impossible path that goes down both sides.

        # Why the base case returns 0, not 1 -> An empty node (None) contributes NOTHING to the depth → 0. The base case must return 0 because None is "no node." The +1 for real nodes happens in the recursive step, so a lone leaf correctly comes out as depth 1.

        # Even though depth is defined top-down, the recursion calculates it bottom-up — the answers are built starting from the leaves and bubbling upward. It dives all the way down first (depth-first, via the stack), hits the base case at the leaves, and then combines answers on the way back up. So even though we measure depth from the top, we compute it from the bottom.

        # The space is the depth of the call stack, which equals the longest chain of active recursive calls — i.e., the tree's height. When the recursion reaches the deepest leaf, that many maxDepth frames are stacked up simultaneously.




        