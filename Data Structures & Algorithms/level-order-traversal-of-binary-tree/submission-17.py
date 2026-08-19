# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS

        result = []

        def dfs(node, depth):
            if not node:
                return 
            
            if depth == len(result):
                result.append([])
            
            result[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return result

        
        # TC: O(n) -> 
        # SC: O(h) -> 


        # Solution Description: DFS can produce level order too, by tracking each node's depth and appending its value to the sublist for that depth. We recurse with a depth parameter; when we reach a new depth for the first time, we create a new sublist. Because DFS visits left before right, values land in left-to-right order within each level. It works, but the level grouping is a manual side effect rather than a natural consequence of the traversal.


        # ----- Deep Dive -----

        # Why "if depth == len(result)" creates a new level -> result is a list of sublists (one per level). len(result) = how many levels we've created so far. When we reach a NEW depth for the first time: depth == len(result)  (this depth's sublist doesn't exist yet) → append a new empty sublist for it. On LATER visits to the same depth: depth < len(result)  (sublist already exists) → skip creation, just append to the existing sublist

        # Why DFS still produces correct left-to-right order -> Even though DFS dives deep (interleaving depths), it always explores the left subtree before the right, so nodes at the same depth are appended left-to-right. The depth-indexed sublists reassemble the correct level order despite the depth-first visit sequence.






        