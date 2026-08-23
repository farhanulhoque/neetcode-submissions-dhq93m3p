# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS

        # Helper carrying maxSoFar — the max value on the path so far
        def dfs(node, maxSoFar):
            # Base case: empty node contributes 0 good nodes
            if not node:
                return 0
            
            # This node is good if it's ≥ the path max (count it as 1, else 0)
            good = 1 if node.val >= maxSoFar else 0

            # Update the running max for this node's children
            maxSoFar = max(node.val, maxSoFar)

            # Add good nodes from the left and right subtree (passing the updated max)
            good += dfs(node.left, maxSoFar)
            good += dfs(node.right, maxSoFar)

            # Return the total good count for this subtree
            return good
        
        # Start at the root; initial max is root.val (the root is always good)
        return dfs(root, root.val)