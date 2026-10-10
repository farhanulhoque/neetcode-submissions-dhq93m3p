class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS directed-cycle detection (with visited set)
        
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        # Set of courses on the current DFS path (the “visiting” state)
        visiting = set()
        
        def dfs(course):
            # If course is already on the current path, we’ve looped back → cycle → return False
            if course in visiting:
                return False
            # If course has no (remaining) prerequisites, it’s finishable → return True (this also catches already-cleared courses)
            if adj[course] == []:
                return True
            
            # Add course to the current path
            visiting.add(course)
            # Explore each of its prerequisites. If any prerequisite leads to a cycle, propagate the failure → return False
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            # Remove course from the current path (backtrack — it’s no longer on the active path)
            visiting.remove(course)
            # Clear course’s prerequisites → marks it fully explored/safe (memoization)
            adj[course] = []

            # Return True — this course is finishable
            return True
        
        # Try every course (the graph may be disconnected). If any course’s DFS finds a cycle, it’s impossible → return False.
        for course in range(numCourses):
            if not dfs(course):
                return False
        # No cycle anywhere → all courses finishable
        return True


        # TC: O(V + E) -> building the adjacency list: O(V) to initialize + O(E) to add edges → O(V + E). The DFS: each node is fully explored once (the state array memoizes — a VISITED node returns immediately), and each edge is traversed once across all DFS calls → O(V + E). O(V + E) overall — the standard graph-traversal bound.
        # SC: O(V + E) -> adj holds V courses + E edges → O(V + E). The visiting set holds at most O(V) (current path) → O(V). Recursion stack up to O(V) deep → O(V). 


        # ----- Deep Dive -----

        # Why adj[course] = [] doubles as “visited/safe” (the clearing trick) -> After a course's prerequisites are ALL successfully explored (no cycle found), you EMPTY its prerequisite list. This does two jobs at once:
                # 1. MEMOIZATION: next time any dfs reaches this course, "adj[course] == []"
                # (returns True instantly — no re-exploring its subtree. This is
                # what keeps the whole thing O(V + E) despite the outer loop.

                # 2. STATE MARKER: an empty preMap = the "VISITED/safe" state. A course with
                # no remaining prerequisites is either a true leaf OR a fully-cleared
                # (already-proven-safe) course — both are finishable, both return True.

                # Why it's safe to clear: once we've confirmed a course has no cycle, that fact never changes. Emptying its prereqs permanently records "safe," and future visits trust it.
        

        # Why visiting.remove(course) must happen (the backtrack) -> The `visiting` set represents courses on the CURRENT DFS path specifically — not all visited courses. So when we finish exploring a course, we must REMOVE it (backtrack), because it's no longer on the active path. Why it matters: a course can be reachable via multiple paths. If we DIDN'T remove it, a later (legitimate, non-cyclic) path reaching it would find it still in `visiting` → FALSE cycle report. remove on exit → `visiting` only ever holds the current path → only true back-edges (loops on the active path) are flagged as cycles. (The `adj[course] = []` on the next line handles "don't re-explore"; the `visiting.remove` handles "I'm off the current path now." Two different jobs.)

        # Why the order — remove from visiting, THEN clear adj -> Both finalization lines run after the exploration loop — that bracketing is what matters (the course stays in visiting throughout its subtree exploration, so a back-edge is caught; and adj keeps its prereqs until they’re explored). The order between the two teardown lines themselves doesn’t affect correctness — they touch different structures and both just mark the course done.








