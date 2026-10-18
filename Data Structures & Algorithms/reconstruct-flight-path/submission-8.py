class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # EULERIAN PATH & HIERHOLZER’S ALGORITHM (DFS)
        
        # Adjacency map: each airport → a min-heap of its destinations (for sorted order)
        adj = defaultdict(list)
        # For each ticket [src, dst], push dst into src’s min-heap (keeps destinations sorted lexicographically)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)
        
        # The result list (will be built in reverse)
        result = []

        # Hierholzer’s DFS helper from airport
        def dfs(airport):
            # While this airport still has unused outgoing tickets
            while adj[airport]:
                # pop the smallest destination (and “use” that ticket by removing it)
                nextDst = heapq.heappop(adj[airport])
                # Recurse into that destination (go deeper, using more tickets)
                dfs(nextDst)
            # Post-order: after all of this airport’s tickets are used, append it to the result
            result.append(airport)
        
        # Start the DFS from JFK
        dfs("JFK")

        # Reverse the result — it was built backward — to get the forward itinerary
        return result[::-1]


        # TC: O(E . log E) -> building the adjacency heaps: E pushes, each O(log E) → O(E · log E). The DFS: each edge is used (popped) exactly once. Each pop is O(log E) (heap removal). Across all E edges → O(E · log E). Appending each node and the final reversal: O(V + E) = O(E). O(E · log E) overall — dominated by the heap operations.
        # SC: O(E) -> the adjacency heaps hold all E edges → O(E). The recursion stack can go up to O(E) deep (a long chain of tickets) → O(E). The result list holds V+1 airports (one per edge traversed, plus start) → O(E).

        # E = number of tickets (edges), V = number of airports (nodes)


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
        

        # Why post-order (append AFTER the while loop) builds the path backward -> We append an airport to `result` only AFTER the while loop — i.e., after ALL its outgoing tickets are used (post-order). The FIRST airport appended is the one where DFS bottoms out — a DEAD END with no outgoing tickets. That dead end is the LAST stop of the itinerary. By appending it first and reversing, it correctly ends up last. As recursion unwinds, earlier airports get appended (in reverse order of when their edges were exhausted). Reversing `result` flips this into the correct forward itinerary, starting at JFK.
                # append order (post-order): [deadend, ..., JFK]
                # reversed:                  [JFK, ..., deadend] 

                # Why not append in pre-order (before the loop)? A naive pre-order greedy walk
                # can get STUCK at a dead end before using all edges — you'd append a partial
                # path and leave tickets unused. Post-order avoids this: it only commits an
                # airport once its edges are fully explored, and the reversal stitches
                # everything correctly.
        

        # Why the min-heap gives lexicographic order -> At each airport, we must choose which ticket to use next. For the LEXICOGRAPHIC-ALLY SMALLEST itinerary, we take the smallest-destination ticket first. The min-heap stores each airport's destinations sorted. heappop always gives the smallest unused destination → we greedily take the smallest next airport.
                # JFK → {ATL, SFO}: heappop gives ATL first (smaller) → explore ATL's subtree before SFO's → ATL appears earlier in the itinerary → smaller lexical order.
                # Popping from the heap ALSO "uses" the ticket (removes that edge), so each ticket is used exactly once — the heap doubles as the edge-removal mechanism.

                # adj["JFK"] = [ATL, SFO]   (heap: ATL smallest)
                # adj["SFO"] = [ATL]
                # adj["ATL"] = [JFK, SFO]   (heap: JFK smallest)

        
        # Why popping the edge ensures “each ticket exactly once” -> heappop REMOVES the destination from the airport's heap. So once we take a ticket (edge), it's gone — we can never use it again.
                # → each ticket is used EXACTLY ONCE (the problem's requirement).
                # → the while loop "while adj[airport]" continues until ALL of an airport's
                # tickets are used (heap empty), then we append and backtrack.

                # This is how we traverse every EDGE exactly once (the Eulerian path property): removing edges as we use them guarantees we don't reuse any, and the DFS structure ensures we eventually use ALL of them.


        # Why result[::-1] — the final reversal -> The post-order DFS appended airports in REVERSE itinerary order (dead end first, JFK last). To get the actual forward itinerary, we reverse.
                # result (post-order) = [last_stop, ..., second_stop, JFK]
                # result[::-1]        = [JFK, second_stop, ..., last_stop]

                # The reversal is the final step that converts the backward-built path into the correct forward sequence. It's essential — without it, you'd return the itinerary in reverse.
 

        # ----- Edge Cases -----

        # Single ticket ([["JFK","ATL"]]) -> dfs("JFK"): pop ATL, dfs("ATL") (no tickets → append ATL), append JFK → result=[ATL, JFK] → reversed → ["JFK","ATL"].

        # Multiple tickets from one airport -> The min-heap orders them; smallest taken first → lexicographically smallest path.

        # Must take a detour (sub-tour) -> Post-order handles it: the dead-end sub-tour is appended, then the DFS backtracks and continues the main path — reversal splices correctly. This is the case naive greedy fails.

        # Airport visited multiple times -> Fine — Eulerian paths revisit nodes; only edges are used once. The heap per airport tracks remaining tickets. 

        # Guaranteed valid path -> The problem guarantees at least one valid itinerary, so we don’t handle the “no Eulerian path exists” case (which would require degree checks).

        # Cycle back to JFK -> Handled naturally — if JFK has more tickets after a sub-tour returns, the while loop continues from it.






        