# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        
        # Empty tree → depth 0
        if not root:
            return 0
        
        # This is a counter for the number of levels
        level = 0
        # Initialize a Queue seeded with the root — BFS uses a queue (FIFO)
        queue = deque([root])

        # Keep going while there are nodes to process
        while queue:
            # Process exactly one full level — len(q) is captured before the loop, so we only process nodes currently in the queue
            for i in range(len(queue)):
                # Remove the front node (FIFO — first in, first out)
                node = queue.popleft()
                # Queue its left child for the next level
                if node.left:
                    queue.append(node.left)
                # Queue its right child for the next level
                if node.right:
                    queue.append(node.right)
            # After finishing one full level → increment the counter
            level += 1
        
        # Total levels = the depth
        return level
        
        # TC: O(n) -> Each node is enqueued once and dequeued once — 2n operations total
        # SC: O(w) -> The queue holds at most one level at a time; the biggest level has width w. For a balanced tree the bottom level has ~n/2 nodes → O(n); for a skewed tree each level has 1 node → O(1)
        

        # Solution Description: Depth equals the number of levels, we can count levels directly with BFS — process the tree level by level with a queue, incrementing a counter for each level until we run out of nodes. Since depth equals the number of levels, we can count levels directly. BFS processes the tree level by level using a queue: we repeatedly drain the current level entirely (queuing up the next level's children as we go), incrementing a counter once per level. When the queue empties, the counter holds the depth.


        # ----- Deep Dive -----

        # The for i in range(len(q)) level-freezing idiom -> len(q) is evaluated ONCE, at the start of the for loop. At that instant, the queue holds EXACTLY the current level's nodes. The for loop processes precisely those — no more, no less. If we DIDN'T freeze len(q) and instead looped "while q" inside, we'd drain the entire tree in one pass and lose all level boundaries.

        # Why a queue (FIFO), not a stack -> BFS must process nodes in the ORDER they were discovered, so that we finish an entire level before starting the next. A queue (FIFO) does this: first node in is the first processed. A stack (LIFO) would dive deep instead of going level by level. 

        # BFS space depends on the widest level w, not height. This is the opposite of DFS (which depends on height). A bushy, balanced tree makes BFS expensive (O(n) width); a tall, skewed tree makes it cheap (O(1) width).






