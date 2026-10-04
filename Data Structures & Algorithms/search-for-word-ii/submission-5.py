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
        # Create the trie root
        root = TrieNode()
        # Loop over every input word and insert each word into the trie
        for word in words:
            root.addWord(word)

        # Store grid dimensions
        rows, cols = len(board), len(board[0])
        # This collects found words
        result = []
        # This is to store the set of cells used in the current path (visited marking)
        visited = set()

        # DFS helper: (r, c) = current cell, node = current trie node
        def dfs(r, c, node):
            # Out-of-bounds check (row/col), Already-visited check (can't reuse a cell), Trie check: this cell's letter must be a valid next character in the trie. If any of these checks fail, this path is dead → return
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                board[r][c] not in node.children):
                return
            
            # Mark the cell visited
            visited.add((r, c))
            # Descend into the trie child for this cell's letter
            node = node.children[board[r][c]]

            # If this trie node marks the end of a word, record the found word. Then clear the word so we don't record it again.
            if node.word:
                result.append(node.word)
                node.word = None
            
            # Explore the neighbors (below, above, left, right)
            dfs(r - 1, c, node)
            dfs(r + 1, c, node)
            dfs(r, c - 1, node) 
            dfs(r, c + 1, node)

            # Backtrack: unmark the cell so other paths can use it
            visited.remove((r, c))
        
        # Loop over every cell (r, c) as a starting point and start a trie-guided DFS from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        # Return all found words
        return result


        # TC: 
        # SC: 


        # Solution Description: The naive approach runs Word Search once per word — O(W · m · k · 4^L), slow for many words. The trie insight fixes this: build a trie of all words, then do a single DFS from each grid cell, walking the trie and the grid in lockstep. At each grid cell, we check whether its letter is a valid next character in the trie. If so, we descend both the grid (into neighbors) and the trie (into that child), continuing only along paths that spell some word's prefix. When we reach a trie node marked endOfWord, we've found a complete word — record it. The trie acts as a shared roadmap: one traversal checks all words at once, and the trie structure prunes any path that doesn't spell a real prefix.


        # ----- Deep Dive -----

        # 







