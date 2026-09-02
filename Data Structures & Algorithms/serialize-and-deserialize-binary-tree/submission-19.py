# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # BFS level-order
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Empty tree → empty string
        if not root:
            return ""
        
        # This is to collect node values
        result = []
        # queue seeded with the root
        q = deque([root])

        # Process the queue
        while q:
            node = q.popleft()
            # Null node → append "N", skip (don't enqueue its children — it has none)
            if not node:
                result.append("N")
                continue
            # Real node → append its value
            result.append(str(node.val))
            # Enqueue both children (including nulls — they'll become "N" markers)
            q.append(node.left)
            q.append(node.right)
        
        # Join into a string
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Empty string → empty tree
        if not data:
            return None

        # Split the values
        values = data.split(",")
        # The first value is the root (preorder)
        root = TreeNode(int(values[0]))
        
        # Queue with the root
        q = deque([root])
        # i points to the next value to assign
        i = 1

        # Process nodes in the queue
        while q:
            node = q.popleft()

            # If the next value isn't "N", it's the left child → create and enqueue it
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            # Advance past the left token
            i += 1

            # If the next value isn't "N", it's the right child → create and enqueue it
            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            # Advance past the right value
            i += 1
            
        # Return the root
        return root
            








