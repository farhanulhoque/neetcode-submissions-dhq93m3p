class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)
        wordList.append(beginWord)

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
                        if nei  not in visited:
                            visited.add(nei)
                            q.append(nei)
            length += 1
        
        return 0