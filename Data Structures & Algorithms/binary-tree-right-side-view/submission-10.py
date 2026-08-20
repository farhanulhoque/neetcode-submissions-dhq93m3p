# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative DFS

        result = []
        if not root:
            return result
        
        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()
            
            if depth == len(result):
                result.append(node.val)
            
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return result