# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            q1.append(node1.left)
            q2.append(node2.left)
            q1.append(node1.right)
            q2.append(node2.right)
        
        return True

        # TC: O(n) -> Compare nodes in lockstep, stopping at the first mismatch. Worst case O(n) for identical trees
        # SC: O(h) -> The queues hold up to a full level's width of nodes (plus None placeholders). For a balanced tree, that's O(n) at the widest level


        # Solution Description: BFS is actually a reasonable fit here (unlike Diameter/Balanced), because Same Tree isn't a bottom-up problem — we just compare corresponding nodes, and any traversal order works as long as both trees are walked identically. We use two queues (one per tree), dequeue corresponding nodes in lockstep, and compare them. Children are enqueued in the same order for both trees.


        # ----- Deep Dive -----

        # 






