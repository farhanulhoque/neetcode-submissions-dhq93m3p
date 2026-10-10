class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS directed-cycle detection (3 state)

        if not prerequisites:
            return True

        # Build the adjacency list: each course maps to an (initially empty) list of its prerequisites
        adj = {i: [] for i in range(numCourses)}
        # For each prerequisite pair [a, b], add edge a → b (course a depends on b)
        for a, b in prerequisites:
            adj[a].append(b)
        
        # State array: 0 = unvisited, 1 = visiting (on the current DFS path), 2 = fully visited (safe)
        state = [0] * numCourses

        # DFS helper: returns True if course can be finished (no cycle through it)
        def dfs(course):
            # If this course is currently visiting (1), we’ve looped back to a node on our own path → cycle → return False.
            if state[course] == 1:
                return False
            # If this course is fully visited (2), it was already checked and found safe → return True (no need to re-explore).
            if state[course] == 2:
                return True

            # Mark this course visiting — it’s now on the current path
            state[course] = 1
            # Explore each of its prerequisites. If any prerequisite leads to a cycle, propagate the failure → return False
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            # All prerequisites are fine → mark this course fully visited (done, safe)
            state[course] = 2
            # Return True — this course is finishable
            return True
        
        # Try every course (the graph may be disconnected). If any course’s DFS finds a cycle, it’s impossible → return False.
        for course in range(numCourses):
            if not dfs(course):
                return False

        # No cycle anywhere → all courses finishable 
        return True


        # TC: O(V + E) -> building the adjacency list: O(V) to initialize + O(E) to add edges → O(V + E). The DFS: each node is fully explored once (the state array memoizes — a VISITED node returns immediately), and each edge is traversed once across all DFS calls → O(V + E). O(V + E) overall — the standard graph-traversal bound.
        # SC: O(V + E) -> the adjacency list holds V nodes + E edges → O(V + E). The state array is size V → O(V). The recursion stack can go O(V) deep (a long dependency chain) → O(V). O(V + E) total.

        # V = numCourses (nodes), E = number of prerequisites (edges).


        # Solution Description: Think of courses as nodes and prerequisites as directed edges: [a, b] means “a depends on b” (you need b before a). You can finish all courses if and only if there’s no cycle — a cycle (like a needs b, b needs a) is a circular dependency that can never be resolved. So the problem is cycle detection in a directed graph. We build an adjacency list (each course → its prerequisites), then DFS from each course. The key is a three-state marker per node: unvisited, visiting (currently on the DFS path), and visited (fully explored, safe). If the DFS ever reaches a node that’s already visiting — meaning we looped back to a node still on our current path — that’s a cycle, so return false. If we explore everything with no such loop, all courses are finishable.


        # ----- Deep Dive -----

        # Why “finish all courses” = “no cycle” -> A prerequisite [a, b] means "do b before a" — a directed dependency. 
                # If there's a CYCLE, say a → b → c → a: to take a, you need b; to take b, you need c; to take c, you need a... → circular dependency, impossible to ever start → can't finish. 
                # If there's NO cycle (the graph is a DAG — directed acyclic graph): you can always find some course with all prerequisites met, take it, then another, etc., until all are done. → finishable.
                # So: can finish all courses ⟺ the dependency graph has no cycle. The whole problem reduces to "does this directed graph contain a cycle?"
        

        # Why THREE states, not just visited/unvisited -> In undirected grids, "visited or not" sufficed — we just needed to avoid re-processing cells. 
                # For DIRECTED cycle detection, we need to distinguish:
                    # 1 (VISITING): this node is on the CURRENT DFS path — we're still exploring its descendants. Reaching it again means we LOOPED BACK → cycle.
                    # 2 (VISITED):  this node is FULLY explored and found safe — reaching it again is FINE (it's a shared dependency, not a cycle).
                # Why the distinction matters — two nodes can both point to a third:
                    # 0 → 2
                    # 1 → 2
                # DFS(0) explores 2, marks it VISITED(2). Later DFS(1) reaches 2 again. This is NOT a cycle — 2 is just a shared prerequisite. State 2 says "safe, don't panic." A binary "visited" couldn't tell this apart from a cycle. Only revisiting a VISITING(1) node — one still on the current path — is a cycle.
                # The three states track WHERE in its lifecycle a node is:
                    # 0: haven't started it
                    # 1: in the middle of exploring it (on the stack / current path)
                    # 2: finished exploring it (off the path, confirmed safe)


        # Why marking VISITING(1) then VISITED(2) brackets the recursion -> The two marks BRACKET the exploration of a node's descendants:
                # mark 1 (VISITING) → "I'm starting to explore this node and everything
                #                     below it. It's on my current path."
                # ... explore all prerequisites (the node stays VISITING throughout) ...
                # mark 2 (VISITED) → "I've fully explored this node and all its
                #                    descendants, no cycle found. It's off my path now."

                # So a node is VISITING exactly while we're exploring its subtree — which is exactly when a back-edge to it would form a cycle. Once we finish (mark 2), the node leaves the "current path," so future visits to it are safe shared-dependency hits, not cycles. This bracketing is the directed-graph analogue of the 'visited'-flag postorder trick from Trees — mark on entry, finalize on exit.


        # Why we DFS from every course -> The dependency graph may be DISCONNECTED — not all courses are reachable from a single starting course. A cycle could exist in a component we'd never reach from course 0. So we launch a DFS from EVERY course. The state array ensures we don't redo work: a course already marked VISITED(2) returns True immediately, so each node is fully explored only once across all the launches. Total work stays O(V + E) despite the outer loop, because the state array memoizes completed nodes.


        # ----- Edge Cases -----

        # No prerequisites (empty list) -> 





