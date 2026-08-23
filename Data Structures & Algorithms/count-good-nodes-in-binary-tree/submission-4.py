# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS

        def dfs(node, maxSoFar):
            if not node:
                return 0
            
            good = 1 if node.val >= maxSoFar else 0

            maxSoFar = max(node.val, maxSoFar)

            good += dfs(node.left, maxSoFar)
            good += dfs(node.right, maxSoFar)

            return good
        
        return dfs(root, root.val)