# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # BFS

        if not subRoot:
            return True
        if not root:
            return False
        
        q = deque([root])

        while q:
            node = q.popleft()
            if self.isSameTree(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False
    
    def isSameTree(self, p, q):
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            node1, node2 = q1.popleft(), q2.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            q1.append(node1.left)
            q2.append(node2.left)
            q1.append(node1.right)
            q2.append(node2.right)
        
        return True




        