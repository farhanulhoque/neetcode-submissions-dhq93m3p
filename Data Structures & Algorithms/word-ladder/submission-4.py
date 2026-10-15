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


        # TC: O(N · L²) -> building the pattern map: N words × L wildcard patterns each × O(L) to build each pattern (string slicing) = O(N · L²). BFS: each word is visited once. For each, we generate L patterns (O(L) each to build = O(L²) per word) and scan matching words. Across all words, this is O(N · L²) (plus edge traversals, bounded by the total pattern-group sizes). O(N · L²) overall.
        # SC: O(N · L²) -> the pattern map stores N words × L patterns, each pattern a string of length L → O(N · L²). The visited set and queue hold up to N words → O(N · L). O(N · L²) dominated by the pattern map.

        # Variables: N = number of words, L = word length.


        # Solution Description: Picture each word as a node. Two words are connected if they differ by exactly one letter (you can transform one into the other in a single step). The question “fewest words to get from beginWord to endWord” becomes “shortest path in this graph” — and for an unweighted graph, that’s BFS. The efficiency challenge: naively checking every pair of words for one-letter difference is slow. Instead, we build an adjacency map keyed by patterns: for each word, generate patterns by replacing each position with * (e.g. hot → *ot, h*t, ho*). Words sharing a pattern differ by exactly one letter, so they’re neighbors. Then BFS from beginWord, counting levels. The first time we reach endWord, the level count is the shortest transformation length.


        # ----- Deep Dive -----

        # Recognizing this as a graph / shortest-path problem -> There's NO explicit graph in the problem. But reframe it:
                # each WORD = a NODE.
                # two words differing by exactly ONE letter = an EDGE between them.
                # a transformation sequence = a PATH through this graph.
                # "minimum number of words" = SHORTEST PATH length.

                # Once you see it this way, the algorithm is obvious: shortest path in an UNWEIGHTED graph = BFS. (Every transformation is "one step," so all edges have equal weight → BFS gives the shortest.)\
                #   beginWord ──(change 1 letter)──> word2 ──> word3 ──> ... ──> endWord. We want the FEWEST hops → BFS.
        

        # The pattern/wildcard trick for fast adjacency (the efficiency key) -> NAIVE adjacency: to find a word's neighbors, compare it against EVERY other word, checking if they differ by one letter. → N words × N comparisons × L chars = O(N² · L). Too slow for big N.
                # PATTERN TRICK: two words are one-letter-apart ⟺ they share a wildcard pattern. "hot" and "dot" both match "*ot" → they differ only at position 0 → neighbors!
                # Build a map: for each word, generate L patterns (one per position replaced by *), and group words under each pattern. Words sharing a pattern are mutual neighbors.
                    # patterns["*ot"] = ["hot", "dot", "lot"]  → all pairwise one-letter-apart.
                    # patterns["h*t"] = ["hot", "hit"]         → neighbors.
                # To find a word's neighbors: generate its L patterns, look each up in the map, and collect the matching words. → O(L) pattern lookups instead of O(N·L) comparisons. Much faster.
                # Why it works: replacing position i with * and matching means "same everywhere EXCEPT position i" = "differ at exactly position i" = one-letter-apart. The pattern is a canonical key that groups all words differing only at that spot.
        

        # Why BFS (not DFS) and why level-counting gives the answer -> BFS, not DFS, because we want the SHORTEST path. BFS explores level by level: all words 1 transformation away, then all 2 away, etc. The FIRST time we reach endWord, it's via the fewest transformations. DFS would plunge down one transformation chain and might reach endWord via a LONG path first → wrong (not shortest). BFS's level-order guarantees shortest.
                # Level counting (the for-range(len(q)) idiom from Trees): each BFS level = one transformation step. We increment `length` per level. When we dequeue endWord, `length` holds the number of words in the shortest sequence.
                # length starts at 1 (beginWord counts as the first word in the sequence).
                #     each level adds 1 (one more transformation).
                #      → reaching endWord returns the sequence length (word count).
        

        # Why mark visited on enqueue (avoiding revisits) -> The word graph has CYCLES and shared neighbors (many words interconnect). Without a visited set, BFS would revisit words endlessly → infinite loop / huge slowdown. We mark a word visited WHEN we enqueue it (not when we dequeue), the universal BFS rule: a word reachable from multiple current-level words would otherwise be nenqueued multiple times → processed repeatedly. Marking on enqueue ensures each word enters the queue exactly once.
                # also: because BFS reaches each word by its SHORTEST path first, once visited we never need to revisit (a later path can't be shorter) → safe to skip.


        # ----- Edge Cases -----

        # endWord not in wordList -> The Line 1 guard returns 0 immediately — no valid target exists.

        # beginWord == endWord -> If endWord is in the list, BFS dequeues beginWord first, matches word == endWord, returns length=1. (Depends on problem’s convention; typically handled by the match check.)

        # No transformation path exists -> BFS exhausts the queue without reaching endWord → returns 0

        # beginWord not in wordList -> Fine — we append it to the list (Line 4) so its patterns are indexed and it’s the BFS start. It needn’t be in the original list.

        # Direct neighbors (one step away) -> beginWord → endWord in one transformation → BFS reaches endWord at level 2 → returns 2.

        # Single-letter words -> Each word has one pattern (*); all single-letter words are mutually connected. Handled naturally.

        # Duplicate-free list (given) -> Guaranteed distinct, so no dedup concerns beyond the visited set.






        