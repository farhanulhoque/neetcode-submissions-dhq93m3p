class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # DFS Topological sort

        # Build the node set: every unique character across all words → an empty adjacency set each
        adj = {c: set() for word in words for c in word}

        # Compare each adjacent pair of words in the words list
        for i in range(len(words) - 1):  
            # Extract the words w1 (earlier) and w2 (later) in the sorted list
            w1, w2 = words[i], words[i + 1]  

            # Get the length to compare up to (the shorter word’s length)
            minLen = min(len(w1), len(w2))   
            # Invalid-prefix check: if w1 is longer than w2 but w2 is a prefix of w1   
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:  
                # the ordering is impossible (a longer word can’t sort before its own prefix) → return ""
                return ""   

            # Scan character positions up to minLen  
            for j in range(minLen):   
                # find the first position where the two words differ
                if w1[j] != w2[j]:    
                    # That difference means w1[j] comes before w2[j] → add edge w1[j] → w2[j]
                    adj[w1[j]].add(w2[j])  
                    # Break — only the first difference gives a valid rule (later ones don’t)
                    break                                  
        
        # Map: True = visiting (on path), False = done
        visited = {}
        # The result (built in post-order)
        result = []

        # DFS helper: returns True if a cycle is found
        def dfs(c):
            # If this char is already in visited, return its state (True = cycle if still “visiting”, or already done)
            if c in visited:
                return visited[c]

            # Mark this char as visiting (on the current path)
            visited[c] = True
            # Explore each letter that must come after this one
            for nei in adj[c]:
                # If recursing finds a cycle, propagate True
                if dfs(nei):
                    return True
            # Mark this char fully done
            visited[c] = False

            # Post-order: append after exploring all successors
            result.append(c)
        
        # Run DFS from every character. If any DFS finds a cycle, return ""
        for c in adj:
            if dfs(c):
                return ""
        
        # Reverse the post-order to get the forward topological order
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







