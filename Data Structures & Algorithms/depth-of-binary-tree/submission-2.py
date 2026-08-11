# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS

        # Base case: an empty node has depth 0
        if not root:
            return 0
        
        # Recursively get the depth of the left and right subtree
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        # This node's depth = 1 (for itself) + the depth of the deeper child (longer path).
        return 1 + max(leftDepth, rightDepth)


        # TC: O(n) -> 
        # SC: O(h) -> 

        # Solution Description: The depth of a tree is 1 (for the current node) plus the depth of its deeper subtree. That self-similar definition is naturally recursive: the depth at any node is 1 + max(depth of left, depth of right), with an empty node having depth 0. That's the DFS approach. 


        # ----- Depp Dive -----

        # 




        