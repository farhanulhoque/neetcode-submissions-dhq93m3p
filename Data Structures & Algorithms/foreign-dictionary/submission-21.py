class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # DFS Topological sort

        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):                    
            w1, w2 = words[i], words[i + 1]  
                          
            minLen = min(len(w1), len(w2))                 
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:  
                return ""      
                                            
            for j in range(minLen):                        
                if w1[j] != w2[j]:                         
                    adj[w1[j]].add(w2[j])                  
                    break                                  
        
        visited = {}
        result = []

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False

            result.append(c)

            return False
        
        for c in adj:
            if dfs(c):
                return ""
        
        return "".join(result[::-1])
            


        # TC: 
        # SC: 


        # Solution Description: Each letter is a node. The sorted word list tells us letter-ordering rules: comparing two adjacent words, the first position where they differ reveals that the letter in the earlier word comes before the letter in the later word (that single difference is why the earlier word sorts first). Each such difference is a directed edge. We build the graph by comparing every adjacent pair of words to extract these edges, then topologically sort the letters. If a valid ordering exists (no cycle), it’s the alien alphabet order; if there’s a cycle (contradictory rules), return "". There’s also a crucial invalid-prefix edge case to catch. I’ll use DFS post-order for the sort (Kahn’s works equally well).


        # ----- Deep Dive -----

        # Topological sort -> orders the nodes of a DIRECTED ACYCLIC GRAPH (DAG) so every edge points "forward" — if there's an edge a → b, then a comes before b. A CYCLE makes a valid ordering impossible → detect it and return "".     
                # The NEW challenge in this problem: the graph isn't given. We must BUILD it from the sorted words by extracting "letter X comes before letter Y" rules.
        

        # 



        # ----- Edge Cases -----

        # 







