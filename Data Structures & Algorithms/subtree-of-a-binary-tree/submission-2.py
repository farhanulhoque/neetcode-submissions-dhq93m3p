# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS
        
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

    # TC: O(n . m) -> n = nodes in root, m = nodes in subRoot. The outer traversal visits all n nodes; at each, sameTree can take up to O(m). Worst case, they multiply.The O(n · m) comes from potentially running the full O(m) comparison at each of the n nodes.
    # SC: O(h) -> Recursion depth — the outer O(h_root) plus the inner sameTree's O(h_subRoot), but they don't stack simultaneously in a way that exceeds O(h_root + h_subRoot), dominated by tree height
    # 

    # Solution Description: Recurse through root. At each node, first check if the subtree rooted here matches subRoot (using the sameTree helper). If it does, we're done. Otherwise, recurse into the left and right children — subRoot is a subtree if it matches at this node or somewhere in the left subtree or somewhere in the right subtree.


    # ----- Deep Dive -----

    # 





