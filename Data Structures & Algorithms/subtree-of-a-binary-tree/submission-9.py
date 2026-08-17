# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Iterative DFS

        # Same base cases as before
        if not subRoot:
            return True
        
        if not root:
            return False

        # Stack seeded with root for the outer traversal
        stack = [root]
        # Process until the stack empties
        while stack:
            # Pop the next candidate node (LIFO — depth-first order)
            node = stack.pop()
            # Run sameTree at this node — match → done
            if self.isSameTree(node, subRoot):
                return True
            # Push real children to continue the outer traversal
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        # No match found anywhere → False
        return False

    
    # Helper isSameTree (Iterative)
    def isSameTree(self, p, q):
        # Stack holds pairs (node_from_p, node_from_q) to compare — start with the roots
        stack = [(p, q)]

        # Process until the stack empties
        while stack:
            # Pop a pair of corresponding nodes
            node1, node2 =  stack.pop()

            # Both None → this position matches, skip ahead
            if not node1 and not node2:
                continue
            # One None or values differ → not equal
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Push the left children as a pair
            stack.append((node1.left, node2.left))
            # Push the right children as a pair
            stack.append((node1.right, node2.right))

        # All pairs matched → equal. Return True
        return True
    
    
    # TC: O(n) -> 
    # SC: O(h) -> 

    # Solution Description: Identical to BFS in structure, but the outer traversal uses a stack (LIFO, depth-first) instead of a queue (FIFO, breadth-first). At each popped node, run the recursive sameTree check. No visited flag needed — this isn't a postorder problem; we just visit every node and test it.


    # ----- Deep Dive -----

    # Only the container changes (stack vs queue) -> The iterative DFS and BFS versions differ only in the container: a stack (LIFO, depth-first) vs a queue (FIFO, breadth-first). Both visit every node of root; the traversal order doesn't affect correctness since we're just searching for any matching node.

    # Why no visited flag (unlike Diameter/Balanced) -> No visited flag is needed because isSubtree isn't postorder — testing a node against subRoot doesn't depend on its children's results. We just visit and test each node independently, so a simple push-pop stack suffices.






    
            