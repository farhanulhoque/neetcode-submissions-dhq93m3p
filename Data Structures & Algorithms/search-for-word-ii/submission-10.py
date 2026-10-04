class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    
    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        result = []
        visit = set()

        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]

            if node.word:
                result.append(node.word)
                node.word = None
            
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
