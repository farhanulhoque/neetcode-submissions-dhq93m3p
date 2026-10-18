class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # EULERIAN PATH & HIERHOLZER’S ALGORITHM (DFS)
        
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)
        
        result = []

        def dfs(airport):
            while adj[airport]:
                nextDst = heapq.heappop(adj[airport])
                dfs(nextDst)
            result.append(airport)
        
        dfs("JFK")

        return result[::-1]


        # TC:
        # SC:


        # Solution Description: Each ticket is a directed edge; we need a path from JFK using every edge exactly once — an Eulerian path — and among valid ones, the lexicographically smallest. We build an adjacency map where each airport’s destinations are in a min-heap (so we always pick the smallest next airport). Then Hierholzer’s post-order DFS: from JFK, repeatedly take the smallest outgoing edge (popping it from the heap, “using” the ticket), recursing deeper. When an airport has no more tickets out, we’ve hit a dead end — append it to the result. This builds the itinerary in reverse, so we reverse at the end to get the correct forward order.


        # ----- Deep Dive -----

        # EULERIAN PATH & HIERHOLZER’S ALGORITHM:

                # Eulerian path: traverse ALL edges, each once. Nodes can repeat. his differs from shortest-path (minimize distance) and node-traversal (visit all nodes) — here we must traverse all edges. “Use each ticket exactly once” is exactly the Eulerian-path requirement, since each ticket is a directed edge.

                # The naive hope: just greedily walk edges, appending nodes as you go. But this
                # FAILS — you can walk into a "dead end" before using all edges, getting stuck.

                # Hierholzer's fix: a POST-ORDER DFS.
                #     - from the current node, keep taking outgoing edges (DFS deeper), removing
                #     each edge as you use it.
                #     - when a node has NO more outgoing edges (dead end), add it to the result.
                #     - this builds the path in REVERSE, so reverse the result at the end.

                # Why post-order works: a node gets added to the result only AFTER all its edges
                # are exhausted. The dead-end node is added first (it's where you get stuck), and
                # it ends up LAST after reversal. Nodes you backtrack through get added in reverse
                # order of completion → reversing gives the correct forward path.

                # Intuition — "stuck-point goes last":
                #     you DFS as deep as you can, using edges. When you hit a dead end (no edges
                #     left), that's necessarily the END of the itinerary (or a sub-tour's end).
                #     Add it first. As you backtrack, you add earlier nodes. Reversing puts the
                #     start (JFK) first and the dead-end last → the valid itinerary.

                # Consider: you DFS from JFK, greedily following edges. Suppose you reach a node X
                # that has no more outgoing edges — a DEAD END. This dead end MUST be the final
                # destination of the itinerary (you can't leave it).

                #     So X should be LAST in the itinerary. In post-order, X is added FIRST
                #     (it's where recursion bottoms out). After reversing, X is last. 

                # As the DFS backtracks from X, it may find OTHER unused edges at earlier nodes
                # and explore those sub-tours. Each sub-tour, when exhausted, adds its nodes.
                # Because we add nodes post-order (after exhausting them) and reverse, these
                # sub-tours get "spliced" into the right positions automatically.

                # The magic: post-order naturally handles the case where you must take a detour
                # (sub-tour) before continuing — the detours get inserted correctly on reversal.


        # ----- Edge Cases -----

        # 






        