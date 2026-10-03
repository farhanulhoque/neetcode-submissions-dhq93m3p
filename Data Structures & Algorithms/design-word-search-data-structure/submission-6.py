class TrieNode:
    def __init__(self):
        # children maps each next character to its child node
        self.children = {}
        # endOfWord marks whether a complete word ends at this node
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        # Create the root node (empty prefix)
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Start walking from the root
        cur = self.root

        # Process each character of the word
        for c in word:
            # If there's no child for this character yet, create a new node
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Descend into the child
            cur = cur.children[c]

        # Mark the final node as the end of a complete word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Recursive helper: j = index in word to start from, node = current trie node
        def dfs(j, node):
            # Track the current node as we walk normal characters
            cur = node
            # Process characters from index j onward
            for i in range(j, len(word)):
                # Grab the current character
                c = word[i]

                # If it's a wildcard
                if c == ".":
                    # try every child of the current node
                    for child in cur.children.values():
                        # Recurse: does the rest of the word (from i + 1) match down this child?
                        if dfs(i + 1, child):
                            # If any child leads to a match, return True
                            return True
                    # No child matched the rest → return False
                    return False
                # Otherwise (a normal character)
                else:
                    # If there's no child for this character, no match → return False
                    if c not in cur.children:
                        return False
                    # Descend into the matching child
                    cur = cur.children[c]
            # Reached the end of the word → return whether a word actually ends here
            return cur.endOfWord
        
        # Kick off the search from index 0 at the root
        return dfs(0, self.root)


        # TC: addWord -> O(L) - walk/create one node per character (same as Implement Trie).
        #     search -> 1. No wildcard -> O(L) — a single path walk, one node per character.
        #               2. With wildcard -> O(26^L) — (worst case) every '.' branches into up to 26 children, and if the word is ALL dots, we explore up to 26^L paths. In practice it's far less — tries are sparse, and normal characters don't branch (they follow one path). A tighter bound is O(n) (total nodes), since a single search never revisits a node.
        # SC: addWord -> O(L) - worst case — up to L new nodes.
        #     search -> O(L) - the recursion depth is at most L


        # Solution Description: Adding words is identical to the previous trie problem — walk character by character, creating nodes, and mark endOfWord at the end. The new challenge is search with . wildcards. For a normal character, search follows the single matching child (like before). But a . matches any letter, so at a . we must try every child — if the rest of the word matches down any of them, it's a match. That branching turns search into a recursive DFS: at each position, either follow one specific child (normal char) or recurse into all children (.). This is exactly the backtracking "try all options" pattern, now applied to trie traversal.


        # ----- Deep Dive -----

        # Why search must be recursive now (the wildcard forces branching) -> In Implement Trie, search was a simple LOOP — one child per character, a single path down the trie (single child to follow). A '.' breaks that: it matches ANY letter, so at a '.' there isn't ONE child to follow — there could be MANY. We must try ALL of them and see if ANY leads to a match. "trying all children and seeing if any works" = branching search = DFS/recursion. So search becomes recursive: at a '.', we recurse into every child; for normal chars, we keep walking (no branching needed).

        # The wildcard branch — trying all children with or-style logic -> At a '.', we iterate over EVERY child node and recursively check whether the REST of the word (from i+1) matches starting at that child. 
        #   for each child:
        #     if dfs(i+1, child) succeeds → the '.' can "be" that child's letter → return True (short-circuit — we found a match)

        #     if NO child leads to a match → return False (the '.' can't be satisfied)

        # This is the SEARCHING pattern: return True if ANY branch works (like the 'or' across directions in Word Search). The loop + early return IS the 'or'.

        # Example: searching ".at" with "cat" and "bat" stored.
        # at '.', children of root = {'c':..., 'b':...}
        # try 'c' branch: does "at" match under 'c'? → c→a→t exists, endOfWord → True
        # → return True immediately (don't even try 'b')


        # Why we pass i + 1 to the recursive call -> When a '.' matches some child (consuming the current character at index i), the REST of the word to match starts at i+1, beginning from that child node. dfs(i + 1, child) means: "match word[i+1:] starting at this child node." The '.' consumed word[i]; the child represents having placed one letter; so we recurse to match the remaining characters from the child onward. searching ".at": '.' at i=0 consumes the '.', recurse dfs(1, child) → now match "at" (word[1:]) starting from the child node.

        # Why j lets us resume from any position -> The helper takes a START INDEX j so it can resume matching from the middle of the word (not always from 0). Why needed? When a '.' recurses with dfs(i+1, child), we must continue matching from position i+1 — NOT restart from 0. The loop "for i in range(j, len(word))" picks up where the recursion left off, processing the remaining characters. Normal characters are handled by the LOOP (walking forward within one dfs call); only a '.' triggers a new recursive dfs call with an advanced j. So each dfs call: walks normal chars in a loop until it either finishes the word, hits a dead end, or hits a '.' (which spawns recursive calls and returns).

        # Why the base case is still cur.endOfWord -> After the loop finishes (all characters of the word matched), we're at some node. Just like the previous problem, we return whether a COMPLETE word ends here (endOfWord), not just whether the path exists. Searching "cat" with "cats" stored → walk c→a→t, but that node's endOfWord is False → return False (cat isn't a stored word). The wildcard doesn't change this: '.' affects HOW we reach the end node (by branching), but the success condition is unchanged — a word must END at the final node. Note: in the '.' branch, each recursive dfs(i+1, child) eventually hits this same base case at its own end, so the endOfWord check happens at the end of EVERY path explored.



        


        
