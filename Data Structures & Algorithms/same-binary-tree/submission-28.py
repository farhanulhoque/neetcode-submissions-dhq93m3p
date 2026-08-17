# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS

        # Two queues, one per tree, each seeded with its root
        q1 = deque([p])
        q2 = deque([q])

        # Process while both queues have items
        while q1 and q2:
            # Dequeue the corresponding node from each tree
            node1 = q1.popleft()
            node2 = q2.popleft()

            # Both None → this position matches, skip to next
            if not node1 and not node2:
                continue
            # One None (structure differs) or values differ → not equal
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Enqueue both children of both nodes (including Nones — crucial!)
            q1.append(node1.left)
            q2.append(node2.left)
            q1.append(node1.right)
            q2.append(node2.right)
        
        # All positions matched → equal
        return True


        # TC: O(n) -> Compare nodes in lockstep, stopping at the first mismatch. Worst case O(n) for identical trees
        # SC: O(h) -> The queues hold up to a full level's width of nodes (plus None placeholders). For a balanced tree, that's O(n) at the widest level


        # Solution Description: BFS is actually a reasonable fit here (unlike Diameter/Balanced), because Same Tree isn't a bottom-up problem — we just compare corresponding nodes, and any traversal order works as long as both trees are walked identically. We use two queues (one per tree), dequeue corresponding nodes in lockstep, and compare them. Children are enqueued in the same order for both trees.


        # ----- Deep Dive -----

        # Why we enqueue None children (unlike other BFS problems) -> We're comparing STRUCTURE. A None in one tree must line up with a None (or a real node) in the OTHER tree at the SAME position. If we skipped Nones, the two queues would fall OUT OF SYNC — corresponding positions wouldn't align anymore. In previous BFS problems, we only enqueued REAL children: if node.left: q.append(node.left) 

        # When both dequeued nodes are None, this position matches (both empty). We "continue" to skip the rest of the loop body — specifically, we DON'T try to enqueue None's children (None has no .left/.right).






