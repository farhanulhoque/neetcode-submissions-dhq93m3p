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

        # 






