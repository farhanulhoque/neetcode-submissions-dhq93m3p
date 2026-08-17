# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative DFS

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


        # TC: O(n) -> Each pair compared once; stop at first mismatch. Worst case O(n) for identical trees
        # SC: O(h) -> The stack holds pairs along the current path


        # Solution Description: Same idea as recursive DFS, but with an explicit stack holding pairs of nodes to compare. We pop a pair, check the base cases, and if they match, push both children-pairs. No visited flag is needed here — Same Tree isn't postorder (we don't need children's results before the parent), so a simple stack works cleanly.


        # ----- Deep Dive -----

        # Why the stack holds PAIRS of nodes -> Each stack entry is a pair of corresponding nodes, because comparison always happens between two trees at the same position. Pushing (n1.left, n2.left) mirrors the recursive call isSameTree(p.left, q.left) — the pair travels together.

        # Why NO visited flag is needed here -> We just need to check EVERY pair. Order doesn't matter. So a plain stack (no visited flag) works — much simpler. This is not postorder — a node comparison doesn't depend on its children's results.

        # continue means: "this pair is fine — skip the rest of the loop body and move on to the next pair in the stack. jump back to "while stack:" and pop the next pair. continue is needed because a None node has no .left or .right to push. Once we confirm both nodes are None (a match), we must skip the append lines — otherwise we'd try None.left and crash. continue jumps straight to the next pair. "both None" confirms one position matches, not the whole tree. return True would exit prematurely, skipping unchecked pairs still on the stack. We only return True at the very end, after the stack is fully drained — meaning every pair matched.





