# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS In-Order
        
        # Counter for how many nodes we've visited in-order so far
        count = [0]
        # Holds the answer once found. None = not found yet (a list so the nested function can mutate it)
        result = [None]

        # In-order helper
        def inorder(node):
            # Stop if the node is empty or the answer is already found (early exit)
            if not node or result[0] is not None:
                return 
            
            # Recurse left first — smaller values before this node
            inorder(node.left)

            # "Visit" this node → increment the count
            count[0] += 1
            # If this is the kth node visited → record its value and stop
            if count[0] == k:
                result[0] = node.val
                return
            
            # Recurse right — larger values after this node
            inorder(node.right)
        
        # Kick off from the root
        inorder(root)
        # Return the kth smallest
        return result[0]


        # TC: O(h + k) -> Descend the left spine (O(h)) to reach the smallest, then visit k nodes. The guard prevents visiting the rest. Worst case (skewed tree, large k) → O(n)
        # SC: O(h) -> Recursion call stack depth = tree height h. Balanced → O(log n); skewed → O(n)
        # With the early-exit guard, this is O(h + k) — we don't traverse the whole tree. Without the guard, a plain "collect all in-order into a list, return arr[k-1]" version would be O(n) time and O(n) space



        # Solution Description: Recurse in-order (left → node → right), incrementing a counter each time we "visit" a node. When the counter reaches k, we've found the kth smallest — record it and stop descending. A guard skips all remaining work once the answer is found.


        # ----- Deep Dive -----

        # Why counting happens BETWEEN the left and right recursion -> In-order visit order is: left subtree → NODE → right subtree. The count MUST increment at the NODE step (between the two recursions), because that's the moment we're "visiting" this node in sorted order. count before left recursion → would count the node too early (wrong order), count after right recursion → would count it too late (wrong order), count BETWEEN → counts it exactly when it's the next-smallest.

        # The early-exit guard — res[0] is not None -> Once we've found the kth smallest, we DON'T need to visit any more nodes. The guard "res[0] is not None" makes every subsequent recursive call return IMMEDIATELY — so we stop descending into the rest of the tree. Without it: the traversal would keep visiting all remaining nodes (harmless to correctness, but wasteful — O(n) instead of O(h + k)). Using None (not -1) as the sentinel is deliberate: node values could be any integer, but never None.

        # result = 0 is fine for this problem — the guarantee that k is valid means res is always overwritten with the real answer before returning, so the placeholder never matters for correctness. The only reason to prefer None is defensive: since BST values can be 0, using 0 as a placeholder could hide a bug behind a plausible-looking return value, whereas None would make any such bug obvious.




        

        