# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS

        # result holds the best diameter found. Making this a member variable of this class so that it is accessible inside the nested dfs function
        self.result = 0

        # This helper function will return the height of a subtree
        def dfs(node):
            # Base case: an empty node has height 0
            if not node:
                return 0
            
            # Get the height of the left and right subtree
            left = dfs(node.left)
            right = dfs(node.right)

            # The diameter check: path bending through this node = left + right edges. Update result if it's the longest
            self.result = max(self.result, left + right)

            # Return the height: 1 (edge to this node) + the deeper child's height
            return 1 + max(left, right)
        
        # Kick off the DFS from the root
        dfs(root)
        # Return the accumulated best diameter
        return self.result

        # TC: O(n) -> Each node is visited exactly once; O(1) work per node (two comparisons)
        # SC: O(h) -> Recursion call stack depth = tree height h. Balanced → O(log n); skewed → O(n)

        # Solution Description: A single recursive helper returns the height of each subtree. At every node, before returning, it computes the path bending through that node (leftHeight + rightHeight) and updates a shared res variable if that path is the longest seen. The function returns height upward (for the parent's use), while diameter accumulates in res.


        # ----- Deep Dive -----

        # Why the function returns HEIGHT but we WANT diameter -> To compute the diameter AT a node, we need the HEIGHTS of its children. diameter through node = leftHeight + rightHeight. So the function's JOB (return value) is to give heights to parents, while its SIDE EFFECT (updating res) accumulates the diameter. Why we can't just return the diameter directly:  parent doesn't need its child's diameter — it needs the child's HEIGHT to compute ITS OWN diameter. So height must flow up; diameter is collected on the side.

        # Why left + right (no +1) for diameter, but 1 + max for height -> Diameter = left + right because the path bends at the node — you add both downward reaches, and the node is just the turning point (no extra edge). Height = 1 + max(left, right) because you go down one side and the +1 is the edge to that child. Different formulas for different measurements.

        # Why this is postorder (children before parent) -> We MUST compute both children's heights BEFORE we can compute this node's diameter (left + right) or height (1 + max). dive down to children → get their heights → combine at the parent = bottom-up computation. This "children first, then parent" order is called POSTORDER traversal.

        # The height COUNTS NODES on the deepest path. The diameter COUNTS EDGES. 
        # 
        # path = [deepest left node] → ... → node → ... → [deepest right node]
        # 
        # nodes on left portion (below node):  = height(left child)
        # nodes on right portion (below node): = height(right child)
        # plus the node itself:                = 1
        # 
        # total NODES on the path = left + right + 1
        # total EDGES on the path = (total nodes) - 1 = left + right + 1 - 1 = left + right
        # 
        # So diameter = left + right EDGES, where left/right are the children's heights (node counts).
        # 
        # The "-1" (edges = nodes - 1) exactly cancels the "+1" (the node itself) → leaving just left + right




        
