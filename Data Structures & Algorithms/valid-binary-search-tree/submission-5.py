# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS

        # Helper carrying the valid range (low, high) for this node
        def valid(node, low, high):
            # Base case: empty node is trivially a valid BST
            if not node:
                return True
            
            # The node must be strictly within (low, high) — else invalid
            if not low < node.val < high:
                return False
            
            return (valid(node.left, low, node.val) and valid(node.right, node.val, high))
        
        return valid(root, float("-inf"), float("inf"))


        # TC: O(n) -> 
        # SC: O(h) -> 


        # Solution Description: Recurse carrying a valid range (low, high) for the current node. A node is valid only if low < node.val < high. Going left, tighten high to node.val (left descendants must all be smaller). Going right, tighten low to node.val. The whole tree is a valid BST if every node satisfies its range.


        # ----- Deep Dive -----

        # 






