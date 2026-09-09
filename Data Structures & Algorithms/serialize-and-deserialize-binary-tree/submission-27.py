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
    

    # TC: Serialize time -> O(n) - Each node enqueued/dequeued once, Deserialize time -> O(n) - Each token processed once
    # SC: O(n) -> The queue holds up to a level's width; the string is O(n)


    # Solution Description: Serialize with level-order (BFS), recording null markers for missing children, and deserialize by reading values level by level, wiring up children as we go. 


    # ----- Deep Dive -----

    # Why we enqueue null children in serialize (but skip their children) -> Null children are enqueued (so they're recorded as "N") but not expanded (a null has no children to enqueue). The continue after appending "N" skips the child-enqueuing step. This records structure without descending into nonexistent children.

    # How deserialize pairs the values with queued parents -> The queue holds nodes that still need their children assigned. The values are in level order, so the next two values after a node ARE its left and right children. Dequeue a parent → next value = its left, value after = its right → wire them up, enqueue any real children (they'll need children too). The pointer i marches through values two-at-a-time (left, right per parent).
            








