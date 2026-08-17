# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS
        
        # Empty subRoot is a subtree of anything (vacuously true)
        if not subRoot:
            return True
        
        # root is empty but subRoot isn't → can't contain it → False
        if not root:
            return False

        # Does the subtree rooted here match subRoot? If yes, found it
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, check if it matches somewhere in the left subtree or the right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    # Helper isSameTree. 
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both empty → match
        if not p and not q:
            return True
        # One empty or values differ → not the same
        if not p or not q or p.val != q.val:
            return False
        # Recurse: both left subtrees match and both right subtrees match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

    # TC: O(n . m) -> n = nodes in root, m = nodes in subRoot. The outer traversal visits all n nodes; at each, sameTree can take up to O(m). Worst case, they multiply.The O(n · m) comes from potentially running the full O(m) comparison at each of the n nodes.
    # SC: O(h) -> Recursion depth — the outer O(h_root) plus the inner sameTree's O(h_subRoot), but they don't stack simultaneously in a way that exceeds O(h_root + h_subRoot), dominated by tree height
    

    # Solution Description: Recurse through root. At each node, first check if the subtree rooted here matches subRoot (using the sameTree helper). If it does, we're done. Otherwise, recurse into the left and right children — subRoot is a subtree if it matches at this node or somewhere in the left subtree or somewhere in the right subtree.


    # ----- Deep Dive -----

    # The two-layer recursion — outer walk, inner compare -> There are TWO separate recursions doing TWO different jobs: 1. OUTER (isSubtree): "visit every node in root as a candidate match point" → recurses on root.left, root.right. 2. INNER (sameTree):  "is THIS subtree identical to subRoot?" → recurses on both trees in parallel (the Same Tree logic). At each node the outer walk reaches, it fires off a full inner comparison.

    # Why or between the recursive calls (vs and in Same Tree) -> a match anywhere (here, left, or right) is enough. sameTree uses AND because equality requires everything to match. The logical operator flips based on whether you're searching (OR) or verifying (AND).

    # Why check sameTree at every node (the base-case ordering) -> The order matters: 1. subRoot empty → True (empty tree is a subtree of anything). 2. root empty (but subRoot isn't) → False (nothing left to match). 3. sameTree here? → if yes, done 4. otherwise, search deeper (left or right). Check 2 comes AFTER check 1: we only declare "root empty = False" once we know subRoot is NON-empty (if both were empty, check 1 caught it).

    # Why we can't just call sameTree(root, subRoot) once -> sameTree(root, subRoot) only checks if root ITSELF (the whole tree) is identical to subRoot. But subRoot could match a subtree DEEP inside root, not at the top! So we must try sameTree at EVERY node, not just the root. That's why isSubtree traverses — to test each node as a candidate.





