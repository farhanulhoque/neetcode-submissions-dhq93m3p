class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS 

        # If endWord isn’t in the word list, it’s unreachable → return 0 (no valid transformation)
        if endWord not in wordList:
            return 0
        
        # Map from a pattern (like h*t) to the list of words matching it (h*t: hot, dot,...)
        patterns = defaultdict(list)
        # Add beginWord to the list so its patterns are indexed too
        wordList.append(beginWord)
        # Loop through each word in the word list
        for word in wordList:
            # for each character position
            for i in range(len(word)):
                # build the pattern by replacing that position with *
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)
        
        visited = set(beginWord)
        q = deque([beginWord])
        length = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return length
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in patterns[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            length += 1
        
        return 0


        # TC:
        # SC:


        # Solution Description: Picture each word as a node. Two words are connected if they differ by exactly one letter (you can transform one into the other in a single step). The question “fewest words to get from beginWord to endWord” becomes “shortest path in this graph” — and for an unweighted graph, that’s BFS. The efficiency challenge: naively checking every pair of words for one-letter difference is slow. Instead, we build an adjacency map keyed by patterns: for each word, generate patterns by replacing each position with * (e.g. hot → *ot, h*t, ho*). Words sharing a pattern differ by exactly one letter, so they’re neighbors. Then BFS from beginWord, counting levels. The first time we reach endWord, the level count is the shortest transformation length.


        # ----- Deep Dive -----

        # There’s no explicit graph given, but if you model each word as a node and connect words that differ by one letter, finding the shortest transformation is just BFS for shortest path


        # ----- Edge Cases -----

        # 






        