# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS

        # The result — one value per level
        result = []

        # Empty tree → empty result
        if not root:
            return result
        
        # Queue seeded with the root
        q = deque([root])
        # Process until no nodes remain
        while q:
            # This is to track the last (rightmost) node seen in this level
            rightmost = None
            # Level-freezing idiom: process exactly this level's nodes
            for i in range(len(q)):
                # Dequeue the front node (left-to-right order)
                node = q.popleft()
                # Update rightmost — after the loop, this holds the last node of the level
                rightmost = node
                # Enqueue children for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # The level's last node is the rightmost → record its value
            result.append(rightmost.val)
        
        # Return the top-to-bottom right-side view
        return result


        # TC: O(n) -> Each node enqueued and dequeued once — 2n operations
        # SC: O(n) -> The queue holds up to the widest level (O(n) for a balanced tree's bottom level)


        # Solution Description: The right side view is the rightmost node at each level — the one you'd see looking at the tree from the right. Since "level" is central, BFS is the natural tool: process each level, and record the last node dequeued (which, with left-to-right ordering, is the rightmost). Collecting one rightmost value per level, top to bottom, gives the answer.


        # ----- Deep Dive -----

        # Why the LAST node dequeued is the rightmost -> We enqueue children left-before-right, and process FIFO (left-to-right). So within a level, nodes are dequeued in left-to-right order. The LAST one dequeued is therefore the RIGHTMOST node of that level.

        # Why we track rightmost rather than index the last iteration -> We track rightmost by overwriting it each iteration (last write wins) rather than checking i == len(q) - 1, because len(q) grows as we enqueue children mid-loop — so an index comparison would be wrong. The overwrite approach sidesteps this entirely.

        






