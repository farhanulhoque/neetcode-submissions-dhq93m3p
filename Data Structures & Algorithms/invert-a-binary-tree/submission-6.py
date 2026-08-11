# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative

        if not root:
            return None
        
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root

        # TC: O(n)
        # SC: O(n)

        # This does the same thing without recursion — a stack holds nodes to process, and we swap each node's children as we pop it. It's O(n) time, and the stack can hold up to O(n) nodes. Useful to know because it avoids recursion depth limits on very deep trees.
