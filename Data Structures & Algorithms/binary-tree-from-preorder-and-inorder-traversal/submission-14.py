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

        # Why the hashmap makes it O(1) instead of O(n) -> Clean version: mid = inorder.index(val) → SCANS inorder → O(n) per node → O(n²). Optimized: mid = idx[val] → dict lookup → O(1) per node → O(n). Build the map ONCE upfront. Then every split-point lookup is instant. The hashmap converts the repeated O(n) inorder scan into an O(1) lookup. Values are unique, so each maps to exactly one index. This is what drops the algorithm from O(n²) to O(n).

        # What mid actually means — position AND count -> Because the root sits AT index `mid` in inorder, there are exactly `mid` nodes before it — and those nodes ARE the left subtree. So `mid` has two meanings at once: 1. POSITION: the root's index in inorder (used to split: [left, mid-1] | [mid+1, right]), 2. COUNT: the number of left-subtree nodes. The count is what preorder implicitly relies on, it's why streaming preorder in order lines up correctly with the inorder split.

        # Why preorder needs only a pointer, but inorder needs bounds -> INORDER — we JUMP AROUND it: at each root we split at `mid` and recurse into two SEPARATE ranges ([left, mid-1] and [mid+1, right]) → need bounds to track which range, PREORDER — we consume it STRICTLY LEFT-TO-RIGHT: we build nodes in the exact order preorder lists them (root → left subtree → right subtree) → never jump back → a single forward pointer suffices. The next root is always the next preorder value.

        # Why preIdx must be shared state (self.preIdx) -> preIdx is shared mutable state — every call reads and advances the same pointer, because preorder is consumed once across the whole recursion. A local variable would give each call its own copy, breaking the global left-to-right consumption.

        # Why build LEFT before RIGHT is mandatory -> preIdx marches through preorder in order: root → LEFT subtree → RIGHT subtree. Preorder lays out the ENTIRE left subtree BEFORE the right subtree. So we must CONSUME all the left subtree's preorder values (by building left) BEFORE building the right.

        # Why left > right is the base case -> (left, right) is an inorder range. A valid range has left <= right.\ left > right means the range is EMPTY → no nodes → return None.

        # The algorithm repeats two steps: 1. "What's the root?" → the next preorder value (preIdx points to it), 2. "How do I split?"     → find that root in inorder (idx[val] = mid); left of mid = left subtree, right = right subtree. Then recurse on the left range and the right range. The two optimizations just make those steps fast: 1. idx hashmap → step 2's lookup is instant (no scanning), 2. preIdx + bounds → no array copying (just move a pointer, pass 2 numbers).







