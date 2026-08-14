# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS

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



        # Solution Description: This replaces recursion with an explicit stack while preserving the crucial postorder (children-before-parent) processing. We use a stack and a heights map. The tricky part is achieving postorder iteratively — we process a node only after both its children have been visited, tracking heights in the map so each node can look up its children's heights when it's finally processed.
        
            