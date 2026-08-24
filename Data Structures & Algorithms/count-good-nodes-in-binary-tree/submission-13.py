# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Iterative DFS

        if not root:
            return 0
        
        count = 0
        stack = [(root, root.val)]

        while stack:
            node, maxSoFar = stack.pop()

            if node.val >= maxSoFar:
                count += 1
            
            maxSoFar = max(maxSoFar, node.val)
            
            if node.left:
                stack.append((node.left, maxSoFar))
            if node.right:
                stack.append((node.right, maxSoFar))
        
        return count