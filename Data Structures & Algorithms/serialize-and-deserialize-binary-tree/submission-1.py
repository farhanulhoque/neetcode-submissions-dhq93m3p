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
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None 
            node = TreeNode(int(values[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


    # Solution Description: To serialize, we traverse the tree and write each node's value to a string — crucially including markers for null children, because without them we can't reconstruct the exact structure. To deserialize, we parse the tokens back in the same order and rebuild the tree. The cleanest scheme is preorder (root → left → right) with a null marker (like "N"). Preorder is ideal because the first token is always the next node to create — so deserialization reads tokens left-to-right with a single moving pointer, building the tree top-down.


    # ----- Deep Dive -----

    # 







