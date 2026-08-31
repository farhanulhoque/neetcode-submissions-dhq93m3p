# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # DFS (hashmap + pointer)

        idx = {val: i for i, val in enumerate(inorder)}
        self.preIdx = 0

        def build(left, right):
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


        # TC: O(n) -> Each node created exactly once with O(1) work: one preIdx read, one idx[val] lookup. The hashmap costs O(n) to build upfront. Total O(n)
        # SC: O(n) -> The hashmap holds n entries. The recursion stack is O(h) (up to O(n) for a skewed tree). No array copies. Overall O(n)
        # Compared to the slicing version's O(n²) time and O(n²) space (from repeated scanning and copying), the two optimizations bring both down to O(n). The hashmap eliminates the scan; the bounds-plus-pointer eliminates the copying.


        # Solution Description: Preorder gives roots (root → left → right), so the first value is always the current root. Inorder splits subtrees (left → root → right), so the root's position divides the remaining nodes into left and right. Recursively: take the next root from preorder, find its split point in inorder, build the left subtree from the values before it and the right from the values after. Empty range → no node. Two optimizations make it O(n): a hashmap (value → inorder index) for O(1) split lookups, and index bounds + a forward pointer into preorder instead of slicing. The pointer works because we build nodes in preorder's exact order — so left must be built before right.


        # ----- Deep Dive -----

        # 


