# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # BFS

        # Empty tree → 0 good nodes
        if not root:
            return 0
        
        # This is running count of good nodes
        count = 0
        # Queue of (node, maxSoFar) — seed with the root and its own value as the max
        q = deque([(root, root.val)])

        # Process until the queue empties
        while q:
            # Dequeue a node and its path-max
            node, maxSoFar = q.popleft()

            # It's a good node if node.val >= maxSoFar → increment count
            if node.val >= maxSoFar:
                count += 1
            
            # Compute the updated max for this node's children
            maxSoFar = max(maxSoFar, node.val)

            # Enqueue children with the updated max
            if node.left:
                q.append((node.left, maxSoFar))
            if node.right:
                q.append((node.right, maxSoFar))

        # Return the total good count    
        return count

        # TC: O(n) -> Each node enqueued and dequeued once
        # SC: O(n) -> 


        # Solution Description: BFS works cleanly here because "good" depends only on the path from root to node, which we can carry in the queue alongside each node. We enqueue (node, maxSoFar) tuples. As we dequeue each, we check if it's good, compute the updated max, and enqueue its children with that max. No level-grouping needed — we just visit every node with its path-max. This is a genuinely valid approach (not contrived), since the state is per-path, not per-level.


        # ----- Deep Dive -----

        # Why we carry maxSoFar in the QUEUE tuple -> BFS carries maxSoFar inside the queue tuple, attached to each node's specific root-to-node path. This replaces the recursion parameter that DFS used. Because the max is per-node (per-path), not per-level, BFS's level-order visiting doesn't corrupt it — each node arrives with its correct path-max.

        # Why no level-freezing idiom is needed here -> No for i in range(len(q)) level-freezing is needed because good Nodes doesn't care about levels — it just visits every node and checks a per-node condition. So we process the queue node-by-node, no level boundaries needed.





