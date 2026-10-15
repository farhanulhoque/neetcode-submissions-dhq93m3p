class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS 

        if endWord not in wordList:
            return 0
        
        patterns = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
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


        # Solution Description:


        # ----- Deep Dive -----

        # There’s no explicit graph given, but if you model each word as a node and connect words that differ by one letter, finding the shortest transformation is just BFS for shortest path


        # ----- Edge Cases -----

        # 






        