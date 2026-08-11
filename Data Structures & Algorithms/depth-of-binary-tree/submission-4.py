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
        
        level = 0
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        
        return level
        
        

        # Solution Description: Depth equals the number of levels, we can count levels directly with BFS — process the tree level by level with a queue, incrementing a counter for each level until we run out of nodes.