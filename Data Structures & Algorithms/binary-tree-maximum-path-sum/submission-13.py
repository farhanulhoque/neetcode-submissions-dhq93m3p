# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # DFS 
        
        # This holds the best path sum found. Initialized to root.val (handles all-negative trees)
        result = [root.val]

        # Helper returning the max downward gain from this node
        def dfs(node):
            # Base case: empty node contributes 0 gain
            if not node:
                return 0
            
            # Get the max gain from the left and right subtree
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            
            # If a downward path sum is negative, we drop it (take 0), because adding negative values only makes the path worse.
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Track the answer: the path bending through this node = node.val + leftMax + rightMax. Update the global max.
            result[0] = max(result[0], node.val + leftMax + rightMax)

            # Return to parent: the straight downward path = node.val + the better ONE branch (a parent can't use a bend)
            return node.val + max(leftMax, rightMax)
        
        # Run the DFS
        dfs(root)
        # Return the best path sum
        return result[0]


        # TC: O(n) -> Every node visited once, O(1) work (a few max operations)
        # SC: O(h) -> Recursion call stack depth = tree height h. Balanced → O(log n); skewed → O(n)
        # Optimal — one pass. The res accumulator travels alongside the recursion (side-effect), so no extra space beyond the call stack.


        # Solution Description: A DFS helper returns the maximum downward gain from a node (the node plus the better of its two branches, clamped so negatives become 0). At each node, we compute the best path bending through it (node.val + leftGain + rightGain) and update a global maximum. The function returns the straight-line gain for the parent; the bending path is only recorded, never returned.

        # ----- Deep Dive -----

        # The return-vs-track split -> Two DIFFERENT quantities: 1. TRACKED (the answer): node.val + leftMax + rightMax = a path that goes UP from the left, through the node, DOWN to the right = the path BENDS at this node (uses BOTH branches), 2.  RETURNED (to parent): node.val + max(leftGain, rightGain) = a path going straight DOWN through one branch only = the parent will EXTEND this path further up. WHY they differ — the "can't reuse a node" rule: If a path already bends at this node (uses both children), it CAN'T also go up to the parent — that would need the node 3 times (left branch, right branch, AND up) → not a valid path. So: a BENDING path is a "complete" path (record it, it ends here). a STRAIGHT path can be extended by the parent (return it).

        # Why we clamp gains with max(leftMax/rightMax, 0) -> A subtree's best downward gain might be NEGATIVE (all negative values). If including a branch would DECREASE the path sum, we're better off NOT including it — a path can just stop at the current node. If a branch would lower the sum, we treat its contribution as 0 (don't include it). A path can always choose to stop rather than extend into a losing branch.

        # Why result starts at root.val, not 0 -> res starts at root.val (not 0) because the path must be non-empty — for an "all-negative" tree, the answer is the least-negative single node, not 0. Initializing to 0 would wrongly allow an "empty path" answer. The clamping handles dropping branches; the initialization handles the "at least one node" rule.

        # Why this is postorder (children before parent) -> A node's path sum (bending or straight) depends on its children's GAINS → children must be computed BEFORE the parent → postorder (bottom-up). Same structure as Diameter and Balanced — any problem where a node's  answer needs its subtrees' answers is postorder. 






