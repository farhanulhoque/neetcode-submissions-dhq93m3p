# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # BFS

        # Same base cases: empty subRoot → True; empty root (with real subRoot) → False
        if not subRoot:
            return True
        if not root:
            return False
        
        # Queue seeded with root for the outer traversal
        q = deque([root])
        # Process every node of root
        while q:
            # Dequeue the next candidate node
            node = q.popleft()
            # Run sameTree at this node — if it matches subRoot, done
            if self.isSameTree(node, subRoot):
                return True
            # Enqueue real children to continue the outer traversal
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        # Visited every node, no match → False
        return False
    
    
    # Helper isSameTree (BFS version)
    def isSameTree(self, p, q):
        # Two queues, one per tree, each seeded with its root
        q1 = deque([p])
        q2 = deque([q])

        # Process while both queues have items
        while q1 and q2:
            # Dequeue the corresponding node from each tree
            node1 = q1.popleft()
            node2 = q2.popleft()

            # Both None → this position matches, skip to next
            if not node1 and not node2:
                continue
            # One None (structure differs) or values differ → not equal
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Enqueue both children of both nodes (including Nones — crucial!)
            q1.append(node1.left)
            q2.append(node2.left)
            q1.append(node1.right)
            q2.append(node2.right)
        
        # All positions matched → equal
        return True


    # TC: O(n . m) -> 
    # SC: O(w) -> 


    # Solution Description: BFS replaces only the outer traversal — we use a queue to visit every node of root level by level, and at each node, run the same sameTree helper. It's a valid fit because the outer traversal is order-independent — we just need to try every node.




        