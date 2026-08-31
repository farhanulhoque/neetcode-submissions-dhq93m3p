# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # DFS (hashmap + pointer)

        idx = {val: i for i, val in enumerate(inorder)}
        self.preIdx = 0

        def build(left, right):
            if left > right:
                return None

            val = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(val)

            mid = idx[val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)  

            return root
        
        return build(0, len(inorder) - 1)