# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # DFS 

        result = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            result[0] = max(result[0], node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return result[0]

            


        # Solution Description: A DFS helper returns the maximum downward gain from a node (the node plus the better of its two branches, clamped so negatives become 0). At each node, we compute the best path bending through it (node.val + leftGain + rightGain) and update a global maximum. The function returns the straight-line gain for the parent; the bending path is only recorded, never returned.

        # ----- Deep Dive -----

        # 