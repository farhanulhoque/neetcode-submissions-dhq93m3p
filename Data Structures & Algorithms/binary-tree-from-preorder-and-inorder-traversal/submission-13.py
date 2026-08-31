# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # DFS (hashmap + pointer)

        # Build a hashmap mapping each value → its index in inorder. One-time O(n) setup that makes every root-lookup O(1) later
        idx = {val: i for i, val in enumerate(inorder)}
        # This is a single shared pointer into preorder, starting at 0. Tracks which preorder value is the "next root to create." Uses self. so it persists and is shared across all recursive calls
        self.preIdx = 0

        # left and right are index bounds describing the current subtree's range within inorder — no array copying
        def build(left, right):
            # Base case: left > right means the inorder range is empty → no node here → return None
            if left > right:
                return None
            
            # Grab the current root's value — it's always preorder[preIdx] because preorder gives roots in exactly the order we build them
            val = preorder[self.preIdx]
            # Advance preIdx past this value — we've "consumed" it
            self.preIdx += 1
            # Create the node for this root
            root = TreeNode(val)

            # O(1) hashmap lookup for the root's position in inorder — the split point
            mid = idx[val]
            
            # Build the left subtree from the inorder range [left, mid-1] (everything before the root)
            root.left = build(left, mid - 1)
            # Build the right subtree from [mid+1, right] (everything after the root)
            root.right = build(mid + 1, right)

            # Return the assembled subtree
            return root
        
        # Kick off with the full inorder range
        return build(0, len(inorder) - 1)


        # TC: O(n) -> Each node created exactly once with O(1) work: one preIdx read, one idx[val] lookup. The hashmap costs O(n) to build upfront. Total O(n)
        # SC: O(n) -> The hashmap holds n entries. The recursion stack is O(h) (up to O(n) for a skewed tree). No array copies. Overall O(n)
        # Compared to the slicing version's O(n²) time and O(n²) space (from repeated scanning and copying), the two optimizations bring both down to O(n). The hashmap eliminates the scan; the bounds-plus-pointer eliminates the copying.


        # Solution Description: Preorder gives roots (root → left → right), so the first value is always the current root. Inorder splits subtrees (left → root → right), so the root's position divides the remaining nodes into left and right. Recursively: take the next root from preorder, find its split point in inorder, build the left subtree from the values before it and the right from the values after. Empty range → no node. Two optimizations make it O(n): a hashmap (value → inorder index) for O(1) split lookups, and index bounds + a forward pointer into preorder instead of slicing. The pointer works because we build nodes in preorder's exact order — so left must be built before right.


        # ----- Deep Dive -----

        # 


