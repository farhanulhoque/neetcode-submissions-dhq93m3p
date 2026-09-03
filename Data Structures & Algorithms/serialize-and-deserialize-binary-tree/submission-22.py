# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        result = []
        q = deque([root])

        while q:
            node = q.popleft()
            if not node:
                result.append("N")
                continue
            
            result.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        
        return ",".join(result)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        values = data.split(",")
        root = TreeNode(int(values[0]))

        q = deque([root])
        i = 1

        while q:
            node = q.popleft()

            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1

            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1
        
        return root





