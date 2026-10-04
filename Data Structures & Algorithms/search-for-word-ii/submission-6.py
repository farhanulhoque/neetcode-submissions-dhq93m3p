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


        # TC: BUILDING THE TRIE -> O(W . L) - insert W words, each up to L characters.
        #     GRID SEARCH -> O(m * n * 4^L) - we start a DFS from each of the m·k cells. From each start, the DFS explores up to 4 directions, but the TRIE PRUNES paths to at most length L (the longest word) — once we're deeper than any word's prefix, node.children is empty → stop. First step 4 directions, then 3 thereafter → ~4·3^(L-1) per start. This is INDEPENDENT of W (the number of words)! The trie merged all words into one search. Naive would be O(W · m · k · 4^L).

        # SC: BUILDING THE TRIE -> O(W · L) — the trie holds up to W·L nodes (fewer with shared prefixes).
        #     GRID SEARCH -> recursion depth + O(m·k) for the visit set (or O(L) if visit only holds the current path, which it does → at most L cells in the path at once) → O(L) for visit. OVERALL SPACE: O(W · L) — dominated by the trie.


        # Solution Description: The naive approach runs Word Search once per word — O(W · m · k · 4^L), slow for many words. The trie insight fixes this: build a trie of all words, then do a single DFS from each grid cell, walking the trie and the grid in lockstep. At each grid cell, we check whether its letter is a valid next character in the trie. If so, we descend both the grid (into neighbors) and the trie (into that child), continuing only along paths that spell some word's prefix. When we reach a trie node marked endOfWord, we've found a complete word — record it. The trie acts as a shared roadmap: one traversal checks all words at once, and the trie structure prunes any path that doesn't spell a real prefix.


        # ----- Deep Dive -----

        # Why a trie searches ALL words at once ->  
            # NAIVE: run Word Search once per word.
            # for each word: search the whole grid for it → O(W · m · k · 4^L)
            # → re-traverses the grid W times, re-exploring shared prefixes repeatedly.

            # TRIE: build a trie of all words, do ONE DFS per starting cell. At each cell, the trie tells us "is this letter a valid next char for ANY word?" If yes, keep going; if no, STOP (prune) → words sharing prefixes are searched TOGETHER in one descent. 
            # Words ["cat","car","card"] all share "ca" → the DFS walks "ca" ONCE, then branches to t / r (and r→d) — instead of re-walking "ca" 3 times.
            # The trie is a SHARED ROADMAP: one grid traversal follows all word-prefixes simultaneously, and the trie structure stops us the moment a path doesn't spell any word's prefix.
        

        # Why the trie provides pruning (board[r][c] not in node.children) -> At each cell, we only continue if its letter is a valid NEXT character in the trie (i.e., some word's prefix continues with this letter). 
            # if board[r][c] is in node.children → this letter extends a real prefix → go deeper
            # if NOT → no word has this prefix path → DEAD END → stop immediately

            # This is PRUNING via the trie: we never explore grid paths that can't spell any word. The trie "knows" which letters are worth pursuing.

            # searching from a 'z' cell when NO word starts with 'z' → root.children has no 'z' → return instantly, zero wasted work.

            # Compare to naive Word Search: it would explore ALL 4-directional paths and only fail when the word's letters run out. The trie fails paths MUCH earlier (as soon as the prefix isn't in any word). That's the efficiency win.

        
        # Why store the word in the node (not just a bool flag) -> Previous tries used endOfWord = True/False. Here we store the actual WORD string at the end node instead. When the DFS reaches an end node, we need to RECORD the word. If we only had a bool, we'd have to reconstruct the word from the path. Storing the full string lets us append it directly:
            # if node.word:  → this node ends a word
            #     res.append(node.word)  → and here's the word, ready to add
            
            # node.word serves DOUBLE duty:
            # - acts as the "endOfWord" marker (None = not a word end, string = word end)
            # - carries the word string so we don't rebuild it from the grid path.
        

        # Why "node.word = None" after finding (deduplication) -> The same word might be reachable via MULTIPLE grid paths. Without dedup, we'd add it to res multiple times.
            # Setting node.word = None after recording it means: the next time the DFS
            # reaches this end node, node.word is None → we DON'T record it again.

            # "cat" reachable from two different starting cells → first find records it and nulls node.word → second find sees None → skips → no duplicate

            # This is a simple, elegant dedup: "cross off" each word as it's found. (Alternative: use a set for res, but nulling the node is cheaper.)
        

        # The grid backtracking (visit marking) -> Identical to Word Search: a cell can't be reused within one word's path, so we mark it visited before exploring and unmark it after (backtrack).
            # visit.add((r,c)) → this cell is now part of the current path
            # explore neighbors (which will skip (r,c) via the "in visit" check)
            # visit.remove((r,c)) → restore it for OTHER paths
        

        # Why we start a DFS from every cell -> We start a DFS from every cell, each beginning at the trie root — because any word could start anywhere. The trie's root.children tells us which first letters are valid; cells with other letters fail the "not in node.children" check immediately. This is the "try all starting points" wrapper from Word Search, now with the trie pruning most starts instantly.




