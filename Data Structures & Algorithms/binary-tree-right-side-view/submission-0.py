# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        if not root:
            return result
        
        q = deque([root])
        while q:
            rightmost = None
            for i in range(len(q)):
                node = q.popleft()
                rightmost = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(rightmost.val)
        
        return result
