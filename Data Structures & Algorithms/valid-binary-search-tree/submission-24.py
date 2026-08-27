# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS
        
        # Empty tree is a valid BST
        if not root:
            return True
        
        # Queue of (node, low, high) — root starts with the widest range
        q = deque([(root, float("-inf"), float("inf"))])

        # Process until the queue empties
        while q:
            # Dequeue a node and its valid range
            node, low, high = q.popleft()

            # Node must be strictly within (low, high) — else invalid
            if not low < node.val < high:
                return False
            
            # Left child: same low, high tightens to node.val
            if node.left:
                q.append((node.left, low, node.val))
            # Right child: low tightens to node.val, same high
            if node.right:
                q.append((node.right, node.val, high))
        
        # All nodes valid → it's a BST
        return True


        # TC: O(n) -> Each node enqueued and dequeued once; short-circuits on violation
        # SC: O(n) -> The queue holds up to the widest level, each entry a (node, low, high) tuple
        # Valid and clean (state carried per-node). Space is O(n) queue width vs the DFS approaches' O(h). Same complexity class, usual BFS-vs-DFS space tradeoff.


        # Solution Description: BFS works by carrying each node's valid (low, high) range in the queue tuple — same idea as the range DFS, but iterative and breadth-first. We enqueue (node, low, high), check each node against its range, and enqueue children with tightened ranges. Valid here (not contrived) because the range is per-node state, carried in the tuple.


        # ----- Deep Dive -----

        # Why the range travels in the queue tuple ->  BFS bundles the (low, high) range into the queue tuple, replacing the recursion parameter. Since the range is per-node state tied to each node's path, breadth-first visiting order doesn't affect correctness — each node carries its own valid range.







