# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS

        # The result — one sublist per level
        result = []

        # Helper carrying the current depth
        def dfs(node, depth):
            # Base case: empty node → nothing to do
            if not node:
                return 
            
            # First time reaching this depth → create its sublist
            if depth == len(result):
                result.append([])
            
            # Append this node's value to its depth's sublist
            result[depth].append(node.val)

            # Recurse left with depth + 1. Then recurse right with depth + 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        # Start at the root, depth 0
        dfs(root, 0)
        # Return the nested list
        return result

        
        # TC: O(n) -> Each node visited once, O(1) work (append to a sublist)
        # SC: O(h) -> Recursion call stack depth = tree height h. Balanced → O(log n); skewed → O(n)
        # DFS uses O(h) space (call stack) vs BFS's O(n) (queue width). For a balanced tree, DFS's O(log n) beats BFS's O(n) — so DFS is actually more space-efficient here, even though BFS is more natural.


        # Solution Description: DFS can produce level order too, by tracking each node's depth and appending its value to the sublist for that depth. We recurse with a depth parameter; when we reach a new depth for the first time, we create a new sublist. Because DFS visits left before right, values land in left-to-right order within each level. It works, but the level grouping is a manual side effect rather than a natural consequence of the traversal.


        # ----- Deep Dive -----

        # Why "if depth == len(result)" creates a new level -> result is a list of sublists (one per level). len(result) = how many levels we've created so far. When we reach a NEW depth for the first time: depth == len(result)  (this depth's sublist doesn't exist yet) → append a new empty sublist for it. On LATER visits to the same depth: depth < len(result)  (sublist already exists) → skip creation, just append to the existing sublist

        # Why DFS still produces correct left-to-right order -> Even though DFS dives deep (interleaving depths), it always explores the left subtree before the right, so nodes at the same depth are appended left-to-right. The depth-indexed sublists reassemble the correct level order despite the depth-first visit sequence.






        