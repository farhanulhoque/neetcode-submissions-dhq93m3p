# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        diameter = 0
        heights = {}
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if visited:
                leftHeight = heights.get(node.left, 0)
                rightHeight = heights.get(node.right, 0)
                diameter = max(diameter, leftHeight + rightHeight)
                heights[node] = 1 + max(leftHeight, rightHeight)
            else:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
        
        return diameter