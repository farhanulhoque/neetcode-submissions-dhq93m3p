class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True 

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True


    # Solution Description: A trie stores strings by their characters along tree paths. Each node has two things: a map of children (one per possible next character) and a boolean endOfWord flag marking whether a complete word ends at this node. Insert: walk from the root, character by character; for each character, create a child node if it doesn't exist, then descend into it. After the last character, mark that node as endOfWord. Search: walk the path for the word; if any character's child is missing, the word isn't there. If we reach the end, return whether that node is marked endOfWord (a word must have been completed there, not just be a prefix). startsWith: identical walk, but we don't care about endOfWord — reaching the end of the prefix path (regardless of the flag) means the prefix exists.


    # ----- Deep Dive -----

    # 
        
        