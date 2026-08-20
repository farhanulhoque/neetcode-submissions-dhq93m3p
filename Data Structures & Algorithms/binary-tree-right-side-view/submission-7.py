# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # DFS

        # The result — one value per depth
        result = []
        
        # Helper carrying the current depth
        def dfs(node, depth):
            # Base case: empty node → nothing
            if not node:
                return
            
            # First node reached at this depth → it's the rightmost → record it
            if depth == len(result):
                result.append(node.val)
            
            # Recurse right first (so the rightmost node at each depth is seen first). Then recurse left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        # Start at the root, depth 0
        dfs(root, 0)
        # Return the right-side view
        return result
        

        # TC: O(n) -> Every node visited once, O(1) work
        # SC: O(h) -> Recursion call stack depth = tree height h. Balanced → O(log n); skewed → O(n)
        # DFS uses O(h) space vs BFS's O(n) width. On a balanced tree, DFS's O(log n) beats BFS's O(n) — so DFS is more space-efficient here, same as in Level Order.


        # Solution Description: DFS can produce the right-side view with a clever ordering: visit the right child before the left, tracking depth. The first node we reach at each depth is the rightmost (since we go right-first). We record a node's value only if it's the first one seen at its depth — checked by comparing depth to the current result length.


        # ----- Deep Dive -----

        # Why visit RIGHT before LEFT -> We want the RIGHTMOST node at each depth. By recursing RIGHT before LEFT, the FIRST node we reach at any depth is guaranteed to be the rightmost one at that depth (we exhaust the right side before touching the left). 

        # Why if depth == len(result) records only the first per depth -> len(result) = how many depths we've recorded so far.The FIRST node to reach a new depth satisfies depth == len(result) → we record it (and only it). Later nodes at the same depth have depth < len(result) → skipped. Since we go RIGHT-first, that "first node per depth" IS the rightmost.





