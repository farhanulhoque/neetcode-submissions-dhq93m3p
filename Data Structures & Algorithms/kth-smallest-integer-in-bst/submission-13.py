# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS In-Order

        count = [0]
        result = [None]

        def inorder(node):
            if not node or result[0] is not None:
                return 
            
            inorder(node.left)

            count[0] += 1
            if count[0] == k:
                result[0] = node.val
                return
            
            inorder(node.right)
        
        inorder(root)
        return result[0]



        # Solution Description: Recurse in-order (left → node → right), incrementing a counter each time we "visit" a node. When the counter reaches k, we've found the kth smallest — record it and stop descending. A guard skips all remaining work once the answer is found.

        

        