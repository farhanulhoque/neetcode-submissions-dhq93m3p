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

        #  The "for i in range(len(q))" level-freezing idiom -> len(q) is evaluated ONCE at the start of the for loop. At that instant, the queue holds EXACTLY the current level's nodes. The for loop runs exactly that many times → processes exactly this level. Children added during the loop go to the BACK → they're the NEXT level, and the captured count means the for loop WON'T touch them this round.

        # Why FIFO (queue) gives left-to-right order -> The problem wants each level LEFT to RIGHT. We enqueue left child BEFORE right child. FIFO (popleft) processes them in the SAME order they were added. So within a level, nodes come out left-to-right — exactly as required.

        # Why we skip None children -> In Same Tree's BFS, we enqueued None to keep two trees ALIGNED. Here there's only ONE tree and no alignment concern — we just want the actual node values per level. So we skip None (standard traversal). Enqueuing None would add junk we'd have to filter, and could crash on None.val.







