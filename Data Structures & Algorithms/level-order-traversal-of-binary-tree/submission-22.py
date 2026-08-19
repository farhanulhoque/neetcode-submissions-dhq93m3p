# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Iterative DFS

        # This is the result list
        result = []
        # empty tree → empty result
        if not root:
            return result
        
        # Stack of (node, depth) pairs, starting at the root, depth 0
        stack = [(root, 0)]
        # Process until the stack empties
        while stack:
            # Pop a (node, depth) pair
            node, depth = stack.pop()

            # First time at this depth → create its sublist
            if depth == len(result):
                result.append([])

            # Append the value to its depth's sublist
            result[depth].append(node.val)

            # Push the right child first (so it's processed after left)
            if node.right:
                stack.append((node.right, depth + 1))
            # Push the left child second (so it pops first)
            if node.left:
                stack.append((node.left, depth + 1))
        
        # Return the nested list
        return result


        # TC: O(n) ->  
        # SC: O(h) -> 


        # Solution Description: The recursive DFS with the stack made explicit — we push (node, depth) pairs and process them, appending each value to its depth's sublist. One subtlety: a plain stack visits right-before-left (LIFO), so to keep left-to-right order we must push right first, then left, so left pops first.


        # ----- Deep Dive -----

        # Why push RIGHT before LEFT (the reversal trick) -> A stack is LIFO — last pushed is popped FIRST. We want LEFT processed before RIGHT (for left-to-right order). So we push RIGHT first (goes deeper in the stack) and LEFT second (sits on top) → LEFT pops first.

        # Why the depth == len(result) trick still works -> Same trick as recursive DFS: create a sublist the first time we hit a depth. len(result) tracks how many sublists EXIST, not how "full" they are. The first time ANY node reaches a new depth, we create its sublist. Order of creation follows first-arrival, which (with right-before-left pushing) still yields correct per-level left-to-right grouping.




            
