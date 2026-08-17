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
    
            