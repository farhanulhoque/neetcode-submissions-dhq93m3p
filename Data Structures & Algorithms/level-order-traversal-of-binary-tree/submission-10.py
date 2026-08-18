# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS 

        # A list of level-lists
        result = []

        # Empty tree → return an empty list
        if not root:
            return result
        
        # Queue seeded with the root
        q = deque([root])
        # Process until no nodes remain
        while q:
            # Initialize fresh list to collect this level's values
            level = []
            # Loop through current level. len(q) = exactly this level's node count, captured before we add children.
            for i in range(len(q)):
                # Dequeue the front node (FIFO — left-to-right order):
                node = q.popleft()
                # Record its value in the current level's list
                level.append(node.val)
                # Enqueue the left and right child for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # This level is fully collected → append it to the result
            result.append(level)
        
        # Return the nested list
        return result


        # TC: O(n) -> Each node is enqueued once and dequeued once — 2n operations
        # SC: O(n) -> The queue holds up to the widest level (O(n) for a balanced tree's bottom level). The result list also holds all n values, but that's the required output


        # Solution Description: Seed a queue with the root. For each level, capture the queue size (the level's node count), then dequeue exactly that many nodes — collecting their values into a level list and enqueuing their children. Append each level list to the result. This directly produces the level-by-level grouping the problem asks for.


        # ----- Deep Dive -----

        #  




