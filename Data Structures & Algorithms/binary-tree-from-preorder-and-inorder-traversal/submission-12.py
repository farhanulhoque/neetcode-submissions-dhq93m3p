# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Build a hashmap mapping each value → its index in inorder. One-time O(n) setup that makes every root-lookup O(1) later
        idx = {val: i for i, val in enumerate(inorder)}
        # This is a single shared pointer into preorder, starting at 0. Tracks which preorder value is the "next root to create." Uses self. so it persists and is shared across all recursive calls
        self.preIdx = 0

        # left and right are index bounds describing the current subtree's range within inorder — no array copying
        def build(left, right):
            if not preorder or not inorder:
                return None

            # Base case: left > right means the inorder range is empty → no node here → return None
            if left > right:
                return None
            
            val = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(val)

            mid = idx[val]
            
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root
        
        return build(0, len(inorder) - 1)
            