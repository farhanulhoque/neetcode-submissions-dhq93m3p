class TrieNode:
    def __init__(self):
        # children maps each next character to its child node
        self.children = {}
        # endOfWord marks whether a complete word ends at this node
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        # Create the root node — an empty node representing the empty prefix
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start walking from the root
        cur = self.root

        # Process each character of the word in order
        for c in word:
            # If there's no child for this character yet, create a new node for it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Descend into the child for this character
            cur = cur.children[c]

        # After the last character, mark this node as the end of a complete word
        cur.endOfWord = True 

    def search(self, word: str) -> bool:
        # Start walking from the root
        cur = self.root

        # Process each character of the word
        for c in word:
            # If any character's child is missing, the word was never inserted → return False
            if c not in cur.children:
                return False
            # Descend into the child for this character
            cur = cur.children[c]
        
        # Return whether a word actually ends here (not just a prefix)
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Start walking from the root
        cur = self.root

        # Process each character of the prefix
        for c in prefix:
            # If any character's child is missing, no word has this prefix → return False
            if c not in cur.children:
                return False
            # Descend into the child for this character
            cur = cur.children[c]

        # Reached the end of the prefix path → the prefix exists (flag irrelevant)
        return True
    

    # TC: insert -> O(L), walk/create one node per character of the word.
        # search -> O(L), walk one node per character.
        # startsWith -> O(L), walk one node per character.
    # SC: insert -> O(L), worst case — up to L new nodes if none of the word's prefix existed before. (O(1) if the whole path already existed.)
        # search -> O(1), just a moving pointer
        # startsWith -> O(1), just a moving pointer
    # L = length of the word or prefix in the operation.


    # Solution Description: A trie stores strings by their characters along tree paths. Each node has two things: a map of children (one per possible next character) and a boolean endOfWord flag marking whether a complete word ends at this node. Insert: walk from the root, character by character; for each character, create a child node if it doesn't exist, then descend into it. After the last character, mark that node as endOfWord. Search: walk the path for the word; if any character's child is missing, the word isn't there. If we reach the end, return whether that node is marked endOfWord (a word must have been completed there, not just be a prefix). startsWith: identical walk, but we don't care about endOfWord — reaching the end of the prefix path (regardless of the flag) means the prefix exists.


    # ----- Deep Dive -----

    # The node structure — children map + endOfWord flag -> Each node represents a POSITION in some set of strings (a prefix). It holds: 1. children: a map from each possible NEXT character to the node you'd reach by adding that character. e.g. root.children = {'c': node1, 'b': node2} means words start with c or b. 2. endOfWord: whether a complete inserted word ENDS at this node. distinguishes "cat" (a real word) from "ca" (just a prefix of "cat"). A path from root to a node spells out a prefix; the characters are on the EDGES (the map keys), not stored in the nodes themselves. Visual for inserting "cat" and "car":
#                 root
#                  |c
#                 (c)              children={'a':...}
#                  |a
#                 (ca)             children={'t':..., 'r':...}
#                 /t      \r
#               (cat)*    (car)*   * = endOfWord=True

# "ca" is shared; it branches into 't' and 'r'. The shared prefix is stored ONCE.


    # Why insert creates nodes lazily (if c not in cur.children) -> As we walk the word, some prefix nodes may already exist (from earlier inserts that shared this prefix), and some may not. If the child for c DOESN'T exist → create it (we're extending into new territory), if it DOES exist → reuse it (this prefix was already built by another word). Then descend into the child either way. Inserting "car" after "cat": 'c' exists (from "cat") → reuse, 'a' exists (from "cat") → reuse, 'r' doesn't exist → create it → "car" reuses the shared "ca" path, only adding the new 'r' branch.

    # Why search returns cur.endOfWord but startsWith returns True (the key difference) -> Both walk the same path (return False if any character is missing). The difference is what "success" means at the end: search("cat"): 
    # search("cat"): the path c→a→t must exist AND the final node must have
    #     endOfWord=True (a word actually ENDS there).
    #     → if we inserted "cats" but never "cat", search("cat") walks c→a→t
    #       fine, but that node's endOfWord is False → returns False
    #       ("cat" is a prefix of "cats" but not itself an inserted word)
    # 
    # startsWith("cat"): the path c→a→t must exist — that's ALL.
    #     → we don't care if a word ends there. Reaching the end of the
    #       prefix path means SOME word has this prefix → return True.
    #     → startsWith("cat") after inserting "cats" → True (cats has prefix cat)


    # Why the shared walk logic — and why the root represents the empty prefix -> All three methods share the same "walk down one node per character" loop.
    # They differ only in:
    # insert:     creates missing nodes, sets endOfWord at the end
    # search:     returns False on missing, checks endOfWord at the end
    # startsWith: returns False on missing, returns True at the end
    # The ROOT is a special empty node representing the empty prefix "". It has no character of its own — it's just the starting point. Its children are the first characters of all inserted words.

    # The trie's key advantage is prefix operations: because words sharing a prefix share a path, checking a prefix is just walking that path once (O(L)), independent of how many words exist. This is exactly why tries power autocomplete and spell-checkers, where prefix matching is the core operation.


    






    
        
        