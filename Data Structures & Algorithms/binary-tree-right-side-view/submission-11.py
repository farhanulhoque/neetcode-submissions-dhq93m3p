# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative DFS

        # Result list
        result = []
        # empty tree → empty result
        if not root:
            return result
        
        # Stack of (node, depth) pairs, starting at root, depth 0
        stack = [(root, 0)]
        # Process until the stack empties
        while stack:
            # Pop a (node, depth) pair
            node, depth = stack.pop()
            
            # First node at this depth → record it
            if depth == len(result):
                result.append(node.val)
            
            # Push the left child first (processed later)
            if node.left:
                stack.append((node.left, depth + 1))
            # Push the right child second (pops first → processed first)
            if node.right:
                stack.append((node.right, depth + 1))

        # Return the right-side view
        return result


        # TC: O(n) -> Each node pushed and popped once
        # SC: O(h) -> Stack holds up to O(h) nodes along a path. Same O(h) space as recursive DFS. Avoids recursion limits.


        # Solution Description -> The recursive DFS with an explicit stack. We push (node, depth) pairs. To reach the rightmost node first at each depth, we must control push order so that right is processed before left — with a stack (LIFO), that means pushing left first, then right (right pops first). We record a node's value the first time we reach its depth.


        # ----- Deep Dive -----

        # Why push LEFT before RIGHT -> We want RIGHT processed BEFORE left (to reach rightmost first). Stack is LIFO — last pushed pops first. So push LEFT first (goes deeper), RIGHT second (on top) → RIGHT pops first. 

        # Why the first-per-depth trick still holds -> The depth == len(result) first-arrival trick works because right-before-left processing guarantees the first node at each depth is the rightmost.






