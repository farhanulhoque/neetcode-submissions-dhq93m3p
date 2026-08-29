# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterative DFS In-Order (preferred approach)

        # Stack of nodes we've passed but not yet "visited"
        stack = []
        # Initializing a current pointer, starting at the root
        curr = root

        # Keep going while there are nodes waiting on the stack or a node to descend into
        while stack or curr:
            # Dive all the way left, pushing each node — the leftmost is the smallest
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Pop the top → the next node in sorted order
            curr = stack.pop()
            
            # Count it (decrement k)
            k -= 1
            # If k reaches 0, this is the kth smallest → return immediately
            if  k == 0:
                return curr.val
            
            # Otherwise, move to this node's right subtree to continue in-order
            curr = curr.right
        
        # k is out of range
        return -1


        # TC: O(h + k) -> Push the left spine (O(h)), then pop/process exactly k nodes. Stops immediately after — never visits the larger nodes. For a large tree where k is small, this is dramatically better than visiting all n nodes.
        # SC: O(h) -> The stack holds at most a root-to-leftmost-leaf path — the tree's height


        # Solution Description: The classic iterative in-order traversal, which naturally supports early stopping. We use a stack: repeatedly dive as far left as possible (pushing each node), then pop a node (the next-smallest), decrement k, and move to its right subtree. When k hits 0, we've popped the kth smallest — return it immediately, mid-traversal. This clean early stop makes it arguably the best fit for this problem.


        # ----- Deep Dive -----

        # The "dive left, pop, go right" mechanic -> The three phases mirror in-order (left → node → right): PHASE 1 (dive left): push nodes while going left. The stack ends up holding a root-to-leftmost path, with the SMALLEST node on TOP. PHASE 2 (visit): pop the top → that's the next node in sorted order. PHASE 3 (go right): set curr = popped.right. Next loop iteration dives left AGAIN from there, finding the next-smallest in that right subtree. This is the iterative in-order template.

        # Why the outer condition is while stack or curr -> Two ways there's still work to do: 1. curr is not None  → there's a node to dive into (Phase 1 pending), 2. stack is not empty → there are nodes waiting to be visited/gone-right-from. We must continue if EITHER holds: - after popping and going right, curr might be None (no right child) but the stack still has ancestors to visit → keep going, - curr might point to a fresh right subtree while the stack is empty → keep going. Using "stack or curr" covers both. Using only "while stack" would quit too early when curr points to an unexplored right subtree with empty stack. 

        # Natural early termination -> The moment we pop the kth node, we RETURN — mid-traversal. The iterative version stops instantly when k hits 0 — a plain return mid-loop, having touched only the left spine plus k nodes. This is the cleanest possible early termination, and why iterative in-order is the go-to for "kth smallest" — no guard flag, no unwinding, just exit.





