# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS (Optimal)
        
        # This helper returns height — or -1 if unbalanced
        def dfs(node):
            # Base case: empty node has height 0 (and is trivially balanced)
            if not node:
                return 0
            
            # Get left and right subtree's height (or -1 if it's unbalanced)
            leftHeight = dfs(node.left)
            rightHeight =  dfs(node.right)

            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            
            return 1 + max(leftHeight, rightHeight)
        
        return dfs(root) != -1

            

        
