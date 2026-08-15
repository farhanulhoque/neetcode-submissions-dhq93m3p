# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS

        # Both nodes empty → they match (two empty trees are equivalent)
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


        # TC: O(n) -> 
        # SC: O(h) -> 


        # Solution Description: 


        # ----- Deep Dive -----

        # 





        
