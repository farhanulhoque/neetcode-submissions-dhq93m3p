# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # BFS

        if not root:
            return 0
        
        count = 0
        q = deque([(root, root.val)])

        while q:
            node, maxSoFar = q.popleft()

            if node.val >= maxSoFar:
                count += 1
            
            maxSoFar = max(maxSoFar, node.val)

            if node.left:
                q.append((node.left, maxSoFar))
            if node.right:
                q.append((node.right, maxSoFar))
            
        return count