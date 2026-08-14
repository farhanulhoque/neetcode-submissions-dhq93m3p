# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS

        self.result = 0

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.result = max(self.result, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.result

        # TC: O(n) -> 
        # SC: O(h) -> 

        # Solution Description: 


        # ----- Deep Dive -----

        # 




        
