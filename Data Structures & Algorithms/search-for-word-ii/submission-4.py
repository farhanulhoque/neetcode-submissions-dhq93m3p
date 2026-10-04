class TrieNode:
    def __init__(self):
        # children maps each next character to its child node
        self.children = {}
        # word stores the complete word string at its end node (instead of a bool flag)
        self.word = None
    
    # This is to insert a word into the trie
    def addWord(self, word):
        # Start at this node (the root, when called on root)
        cur = self

        # Process each character of the word
        for c in word:
            # If there's no child for this character, create one
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Descend into the child
            cur = cur.children[c]

        # At the end node, store the full word (marks the ending and gives us the string)
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        result = []
        visited = set()

        def dfs(r, c, node):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]

            if node.word:
                result.append(node.word)
                node.word = None
            
            dfs(r - 1, c, node)
            dfs(r + 1, c, node)
            dfs(r, c - 1, node) 
            dfs(r, c + 1, node)

            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return result


        # TC: 
        # SC: 


        # Solution Description: The naive approach runs Word Search once per word — O(W · m · k · 4^L), slow for many words. The trie insight fixes this: build a trie of all words, then do a single DFS from each grid cell, walking the trie and the grid in lockstep. At each grid cell, we check whether its letter is a valid next character in the trie. If so, we descend both the grid (into neighbors) and the trie (into that child), continuing only along paths that spell some word's prefix. When we reach a trie node marked endOfWord, we've found a complete word — record it. The trie acts as a shared roadmap: one traversal checks all words at once, and the trie structure prunes any path that doesn't spell a real prefix.


        # ----- Deep Dive -----

        # 







