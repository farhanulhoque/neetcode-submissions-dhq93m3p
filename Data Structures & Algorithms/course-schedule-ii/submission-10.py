class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS (Post-Order + Cycle Detection)

        # Adjacency list keyed by course: adj[crs] = its prerequisites (course → prereq)
        adj = {i: [] for i in range(numCourses)}
        # For each pair [crs, pre], add edge crs → pre (crs depends on pre)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        # Three-state array: 0 unvisited, 1 visiting (on path), 2 visited (done)
        state = [0] * numCourses

        # The result order
        result = []

        # DFS helper: returns True if crs is cycle-free
        def dfs(course):
            # If course is currently visiting, we looped back → cycle → return False
            if state[course] == 1:
                return False
            # If course is fully visited, already processed and safe → return True
            if state[course] == 2:
                return True
            
            # Mark visiting (on the current path)
            state[course] = 1
            # Explore each prerequisite of this course. If a prerequisite leads to a cycle, propagate failure → False
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            # Mark visited (done)
            state[course] = 2

            # Append crs AFTER its prereqs — post-order placement
            result.append(course)
            # Return True
            return True
        
        # Try every course (disconnected graph). If any DFS finds a cycle, return [] (impossible)
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        # Return the order
        return result


        # TC: O(V + E) -> build adj O(V+E); DFS visits each node once (memoized by state) and each edge once → O(V+E).
        # SC: O(V + E) -> adjacency list O(V+E); state array O(V); recursion stack up to O(V); order list O(V). → O(V + E).


        # Solution Description: DFS with three-state tracking (as in Course Schedule I), but we build the order via post-order: after fully exploring a course’s prerequisites, append the course. This produces the order reversed (a course is added after its prereqs are added), so we reverse at the end. If a cycle is detected, return [].


        # ----- Deep Dive -----

        # Why post-order gives the topological order (no reversal needed here) -> We append a course only AFTER fully exploring (and appending) all its nprerequisites. So each prerequisite lands in `order` BEFORE the course that needs it. append happens in POST-ORDER: children (prereqs) added before the parent (course).
                # Since adj here points course → prerequisite, exploring "down" reaches prerequisites, and appending on the way back up adds prereqs first, then dependents. → prereqs before dependents = valid topological order.

                # prerequisites = [[1,0]]  (1 needs 0), adj[1]=[0]
                # dfs(1): explore pre 0 → dfs(0): adj[0]=[] → append 0 → order=[0]
                #         back in 1 → append 1 → order=[0,1]
                # → [0, 1]: 0 (prereq) before 1 (dependent) — already correct, no reversal!
        
                # IMPORTANT subtlety — edge direction decides whether you reverse:
                #     adj = course → prereq (this code): post-order gives prereqs-first → NO reversal.
                #     adj = prereq → course: post-order gives dependents-first → MUST reverse at end.
                # Here, because edges point to prerequisites and we append post-order, the order comes out correct WITHOUT reversing. (Many DFS solutions use the other edge direction and reverse — both are valid, just be consistent.)
        

        # Why the three-state tracking still detects cycles -> Same as Course Schedule I: the three-state array catches back-edges to a node still on the current DFS path (state 1 = visiting). A cycle makes a valid ordering impossible, so we return []. 
                # The cycle check and the order-building coexist:
                #     - state 1 (visiting): detect cycles (back-edge → return False → [])
                #     - state 2 (visited) + append: build the order in post-order

                # A course is appended ONLY if it (and all its prereqs) are cycle-free — the append happens after the recursion succeeds, so cyclic courses never get added.
        

        # The DFS post-order approach is equally classic as Kahn's — worth knowing because “topological sort = DFS post-order (reversed)”


        # ----- Edge Cases -----

        # Same edge cases as Kahn’s (no prereqs → any order; cycle → []; self-loop → []; disconnected → full order). The DFS version handles them via the three-state cycle check returning [] on any back-edge, and post-order naturally ordering acyclic courses.







