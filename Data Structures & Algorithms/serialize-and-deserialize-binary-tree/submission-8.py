# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # DFS Preorder
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # This is to collect node values here
        result = []

        # Preorder helper
        def dfs(node):
            # Null node → append the marker "N" and return (this is what preserves structure)
            if not node:
                result.append("N")
                return

            # Null node → append the marker "N" and return (this is what preserves structure)
            result.append(str(node.val))

            # Recurse left, then right (preorder: root already written above)
            dfs(node.left)
            dfs(node.right)

        # Run the traversal
        dfs(root)
        # Join the values with commas into the final string
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split the string back into the values
        values = data.split(",")
        # This is the shared pointer into the values list (starts at 0)
        self.i = 0
        
        # Preorder rebuild helper
        def dfs():
            # Current value is "N" → consume it, return None
            if values[self.i] == "N":
                self.i += 1
                return None 
            
            # Otherwise, create a node from the current token
            node = TreeNode(int(values[self.i]))
            # Advance the pointer past this token
            self.i += 1

            # Recursively build the left subtree then the right subtree (consumes the next values)
            node.left = dfs()
            node.right = dfs()

            # Return the assembled node
            return node

        # Kick off — returns the root
        return dfs()
    

    # TC: Serialize time -> O(n) - Visit every node once, O(1) append each, Deserialize time -> O(n) - Consume every token(value) once, O(1) work each (n real nodes + n+1 null markers = O(n) tokens(values))
    # SC: The string/values list holds O(n) values; recursion stack is O(h)
    # Both directions are O(n). The number of null markers is n+1 (a binary tree with n nodes has exactly n+1 null slots), so the total token count is 2n+1 = O(n).


    # Solution Description: To serialize, we traverse the tree and write each node's value to a string — crucially including markers for null children, because without them we can't reconstruct the exact structure. To deserialize, we parse the tokens back in the same order and rebuild the tree. The cleanest scheme is preorder (root → left → right) with a null marker (like "N"). Preorder is ideal because the first token is always the next node to create — so deserialization reads tokens left-to-right with a single moving pointer, building the tree top-down.


    # ----- Deep Dive -----

    # 







