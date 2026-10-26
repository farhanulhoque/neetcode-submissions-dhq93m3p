class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # DFS Topological sort
        # graph building -> invalid-prefix check -> three-state cycle detection -> post-order + reverse

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
            # If this char is already in visited
            if c in visited:
                # Return its state. Already seen → True (visiting = cycle) or False (done = safe)
                return visited[c]

            # Mark this char as visiting (on the current path)
            visited[c] = True
            # Explore each letter that must come after this one
            for nei in adj[c]:
                # If recursing finds a cycle, propagate True
                if dfs(nei):
                    return True
            # Mark this char fully done (safe)
            visited[c] = False

            # Post-order: append after exploring all successors
            result.append(c)

            # Return False (no cycle through this char)
            return False
        
        # Run DFS from every character. If any DFS finds a cycle (contradictory ordering), return ""
        for c in adj:
            if dfs(c):
                return ""
        
        # Reverse the post-order to get the forward topological order
        return "".join(result[::-1])
            

        # TC: O(N) -> where N is the total characters across all words. Building the node set and extracting edges both scan the input (O(N)), and the topological sort is O(U + E) where U ≤ 26 letters and E ≤ 676 edges — constants. So the input-reading dominates.
        # SC: O(1) -> adjacency map: U nodes + E edges → O(U + E), bounded by 26 + 676 = O(1). Visited map + recursion stack: O(U) ≤ O(26) = O(1). The result: O(U). O(U + E) = O(1) given the fixed 26-letter alphabet (plus O(N) to read input). The algorithm is essentially linear in the input size, with a constant-size graph.

        # Variables: N = total number of characters across all words; U = number of unique letters (≤ 26); E = number of edges (≤ U²).


        # Solution Description: Each letter is a node. The sorted word list tells us letter-ordering rules: comparing two adjacent words, the first position where they differ reveals that the letter in the earlier word comes before the letter in the later word (that single difference is why the earlier word sorts first). Each such difference is a directed edge. We build the graph by comparing every adjacent pair of words to extract these edges, then topologically sort the letters. If a valid ordering exists (no cycle), it’s the alien alphabet order; if there’s a cycle (contradictory rules), return "". There’s also a crucial invalid-prefix edge case to catch. I’ll use DFS post-order for the sort (Kahn’s works equally well).


        # ----- Deep Dive -----

        # Topological sort -> orders the nodes of a DIRECTED ACYCLIC GRAPH (DAG) so every edge points "forward" — if there's an edge a → b, then a comes before b. A CYCLE makes a valid ordering impossible → detect it and return "".     
                # The NEW challenge in this problem: the graph isn't given. We must BUILD it from the sorted words by extracting "letter X comes before letter Y" rules.
        

        # How adjacent words give letter-ordering rules (the core modeling) -> The words are SORTED by the alien order. So for two adjacent words w1, w2 (w1 before w2), w1 ≤ w2 in the alien ordering. The FIRST position where they differ tells us WHY w1 sorts first: w1[j] must be SMALLER (earlier) than w2[j] in the alien alphabet → that's a rule: w1[j] comes before w2[j] → edge w1[j] → w2[j].
                # w1 = "wrt", w2 = "wrf"
                # compare: w==w, r==r, t≠f → FIRST difference at position 2.
                # → 't' comes before 'f' in the alien order → edge t → f.

                # Only the FIRST difference matters — once two words differ at position j, the characters BEFORE j are equal (they tell us nothing), and characters AFTER j are irrelevant (the ordering is already decided by position j). Hence break. Extracting these edges from every adjacent pair builds the constraint graph.
        

        # The invalid-prefix edge case -> Consider two adjacent words where one is a PREFIX of the other: w1 = "abc", w2 = "ab". For w1 to sort BEFORE w2, by the rules, a prefix must come first (shorter before longer when one is a prefix of the other). But here the LONGER word (w1="abc") comes before the SHORTER prefix (w2="ab") — that's IMPOSSIBLE in any valid lexicographic order. "ab" should come before "abc" (prefix rule), but the input has "abc" first → the input is NOT validly sorted → return "". 
                # The check: if w1 is longer than w2 AND w2 is a prefix of w1 (their common part matches), it's invalid.

                #  If we DIDN'T check this: the inner loop finds NO differing character (w2 is fully a prefix), extracts no edge, and we'd WRONGLY proceed as if valid.  So this check is essential — it catches an invalidity that produces no edge.

                # words = ["abc", "ab"]: w1="abc" longer than w2="ab", and w1[:2]=="ab"==w2[:2] → return "" (a longer word can't precede its own prefix)
        

        # The three-state DFS for cycle detection (recap, in a map) -> Same three-state cycle detection from Course Schedule, here using a map:
                # c NOT in visited → unvisited
                # visited[c] == True → VISITING (on the current DFS path)
                # visited[c] == False  → VISITED (fully done, safe)

                # If dfs(c) finds c already "visiting" (True), we've looped back on our own path → a CYCLE → the letter ordering is contradictory → return "". e.g. edges a→b and b→a: dfs(a) visits b, b's dfs visits a (still True / visiting) → cycle detected → "". A cycle means the constraints contradict (a before b AND b before a) → no valid alien order exists.
        

        # Why post-order + reverse gives the ordering -> DFS post-order (from Course Schedule II): a letter is appended AFTER all letters that must come after it are appended. So successors land in res before predecessors → res is in REVERSE topological order → reverse it. 
                # edge t → f means t before f. In post-order, f (a successor) is appended before t. Reversing puts t before f → correct order. This yields a valid alien alphabet ordering respecting all the "before" edges.



        # ----- Edge Cases -----

        # Single word -> No adjacent pairs → no edges; every letter is an isolated node → any order of its unique letters is returned (all valid).

        # Invalid prefix (["abc","ab"]) -> The invalid prefix check catches it → returns "". The critical trap.

        # Cycle in constraints (["a","b","a"] style → a→b, b→a) -> DFS detects the cycle → returns "".

        # All same letters / identical adjacent words -> No differing position → no edge extracted (and not an invalid prefix if equal length) → letters ordered freely.

        # Single character alphabet -> One node, no edges → returns that character.

        # Letters only in one word (isolated nodes) -> Included in adj (Line 1 collects all letters) → appear in the output in some valid position.

        # Multiple valid orderings -> The problem allows any; DFS produces one valid order.







