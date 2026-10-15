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
                # Record this word under that pattern
                patterns[pattern].append(word)
        
        # Visited set, seeded with beginWord (so we don’t revisit it)
        visited = set(beginWord)
        # BFS queue, starting with beginWord
        q = deque([beginWord])
        # length = transformation count; starts at 1 (the beginWord itself counts)
        length = 1

        # BFS until the queue empties
        while q:
            # Level-freezing: process exactly this level (one transformation step)
            for _ in range(len(q)):
                # Dequeue the next word
                word = q.popleft()
                # If it’s the endWord, we’ve reached it → return the current length (shortest)
                if word == endWord:
                    return length
                
                # Loop through each position in the word
                for i in range(len(word)):
                    # build its wildcard pattern
                    pattern = word[:i] + "*" + word[i + 1:]
                    # For each word matching that pattern (a one-letter-apart neighbor)
                    for nei in patterns[pattern]:
                        # if unvisited, mark it visited (on enqueue) and enqueue it for the next level
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            # One full level done → increment the transformation count
            length += 1
        
        # Queue emptied without reaching endWord → no path → return 0
        return 0


        # TC:
        # SC:


        # Solution Description: Picture each word as a node. Two words are connected if they differ by exactly one letter (you can transform one into the other in a single step). The question “fewest words to get from beginWord to endWord” becomes “shortest path in this graph” — and for an unweighted graph, that’s BFS. The efficiency challenge: naively checking every pair of words for one-letter difference is slow. Instead, we build an adjacency map keyed by patterns: for each word, generate patterns by replacing each position with * (e.g. hot → *ot, h*t, ho*). Words sharing a pattern differ by exactly one letter, so they’re neighbors. Then BFS from beginWord, counting levels. The first time we reach endWord, the level count is the shortest transformation length.


        # ----- Deep Dive -----

        # Recognizing this as a graph / shortest-path problem -> There's NO explicit graph in the problem. But reframe it:
                # each WORD = a NODE.
                # two words differing by exactly ONE letter = an EDGE between them.
                # a transformation sequence = a PATH through this graph.
                # "minimum number of words" = SHORTEST PATH length.

                # Once you see it this way, the algorithm is obvious: shortest path in an UNWEIGHTED graph = BFS. (Every transformation is "one step," so all edges have equal weight → BFS gives the shortest.)\
                


        # ----- Edge Cases -----

        # 






        