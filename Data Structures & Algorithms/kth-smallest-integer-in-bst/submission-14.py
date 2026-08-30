# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS In-Order
        
        # Counter for how many nodes we've visited in-order so far
        count = [0]
        # Holds the answer once found. None = not found yet (a list so the nested function can mutate it)
        result = [None]

        # In-order helper
        def inorder(node):
            # Stop if the node is empty or the answer is already found (early exit)
            if not node:
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

        

        