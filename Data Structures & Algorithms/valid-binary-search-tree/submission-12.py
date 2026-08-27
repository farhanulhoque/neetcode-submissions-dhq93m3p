# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # In-order Traversal

        prev = [float("-inf")]

        def inorder(node):
            if not node:
                return True
            
            if not inorder(node.left):
                return False
            
            if node.val <= prev[0]:
                return False
            
            prev[0] = node.val
        
            return inorder(node.right)
        
        return inorder(root)

        

        # Solution Description: This exploits a beautiful BST property: an in-order traversal of a BST visits values in strictly increasing order. So we do an in-order traversal (left → node → right) and check that each value is strictly greater than the previous one. If any value isn't, it's not a valid BST. This is often considered the cleanest BST-validation approach.


        # ----- Deep Dive -----

        # 