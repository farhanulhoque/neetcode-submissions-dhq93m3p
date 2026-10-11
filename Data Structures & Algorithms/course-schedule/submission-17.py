class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS Topological Sort (Kahn's Algorithm)

        # Adj list — but keyed by prerequisite: adj[pre] = courses that depend on pre (edge points forward, prereq → dependent)
        adj = {i: [] for i in range(numCourses)}
        # indegree[crs] = how many prerequisites course crs still needs (starts at 0)
        indegree = [0] * numCourses

        # For each pair [crs, pre] (crs needs pre)
        for crs, pre in prerequisites:
            # add edge pre → crs (taking pre unlocks crs)
            adj[pre].append(crs)
            # increment crs’s in-degree (it has one more prerequisite)
            indegree[crs] += 1
        
        # The BFS queue
        q = deque()
        # Scan every course. If it has no prerequisites (in-degree 0), it’s immediately takeable → seed the queue with it
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        # Counter for how many courses we’ve taken
        taken = 0

        # Process until no more takeable courses remain
        while q:
            # Take the next available course (dequeue)
            course = q.popleft()
            # Count it as taken
            taken += 1

            # For each course that depended on this one
            for nxt in adj[course]:
                # one of its prerequisites is now satisfied → decrement its in-degree
                indegree[nxt] -= 1
                # If that dependent now has zero remaining prerequisites, it’s newly takeable → enqueue it
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        # Finishable if we took all numCourses (no course got stuck in a cycle)
        return taken == numCourses
        

        # TC: O(V + E) -> building adj + in-degrees: O(V) to initialize + O(E) for edges → O(V + E). Seeding the queue: O(V) scan. The BFS: each course is enqueued and dequeued at most ONCE (only when its in-degree hits 0) → O(V) dequeues. Each dequeue processes that course's outgoing edges (decrements dependents) → O(E) total edge work. O(V + E) overall.
        # TC: O(V + E) -> the adjacency list holds V nodes + E edges → O(V + E). The in-degree array is size V → O(V). The queue holds at most O(V) courses → O(V). O(V + E) overall.

        # V = numCourses, E = prerequisites.


        # Solution Description: Instead of DFS cycle detection, Kahn’s algorithm builds a valid ordering and checks whether it covers all courses. Each course has an in-degree = the number of prerequisites it still needs. Courses with in-degree 0 can be taken immediately. We seed a queue with all in-degree-0 courses. Repeatedly: take one (dequeue it, count it), and for each course that depended on it, decrement that course’s in-degree (one prerequisite satisfied). If a dependent’s in-degree drops to 0, it’s now takeable → enqueue it. Continue until the queue empties. If we took all numCourses, there’s no cycle (finishable); if some courses were never takeable (stuck with in-degree > 0 — trapped in a cycle), we took fewer than numCourses → not finishable.


        # ----- Deep Dive -----

        # What “in-degree” means and why the edge direction flips -> IN-DEGREE of a course = how many prerequisites point INTO it = how many courses must be taken before it.
                # indegree[crs] = number of unmet prerequisites of crs.
                # indegree 0 = no prerequisites left = takeable NOW.

                # Edge direction — note it's OPPOSITE the DFS version:
                    # DFS version:   adj[crs] = [its prerequisites]   (course → prereq, "I need these")
                    # Kahn's:        adj[pre] = [its dependents]      (prereq → course, "I unlock these")
                # Why the flip? In Kahn's, when we TAKE a course, we need to find everything it UNLOCKS (its dependents) to decrement their in-degrees. So edges point FROM a prereq TO the courses that depend on it — "finishing me enables these."

                # prerequisites = [[1,0]]  (1 needs 0)
                # DFS:    adj[1] = [0]   (1 points to its prereq 0)
                # Kahn's: adj[0] = [1]   (0 points to 1, which it unlocks)
                #     indegree[1] = 1 (course 1 has one prereq)
        

        # Why we seed in-degree-0 courses and decrement as we go -> The queue always holds courses that are TAKEABLE RIGHT NOW (all prereqs met, in-degree 0). 
                # START: seed with courses that have 0 prereqs — the only ones you can take without taking anything else first.
                # EACH STEP: take a course → it's now "done" → for every course that depended on it, that dependency is satisfied → decrement their in-degree. If a dependent's in-degree hits 0, ALL its prereqs are now done → it becomes takeable → enqueue it.

                # This mirrors real scheduling: finishing a course opens up the courses that required it. The "unlocking" cascades outward from the no-prereq courses.
        

        # Why taken == numCourses detects a cycle -> If there's NO cycle (a DAG): the unlocking cascade eventually reaches EVERY course — each gets its in-degree driven to 0 and gets taken. taken == numCourses. 
                # If there's a CYCLE, say 0 → 1 → 0: those courses can NEVER reach in-degree 0.
                #     course 0 needs course 1 taken first (indegree ≥ 1)
                #     course 1 needs course 0 taken first (indegree ≥ 1)
                #     neither can EVER be taken → they're never enqueued → never counted. → the queue empties with those courses still stuck → taken < numCourses.
                # So: taken == numCourses ⟺ every course was takeable ⟺ no cycle. The cycle's courses are precisely the ones left with in-degree > 0 when the queue empties — they're waiting on each other forever.

                # prerequisites = [[0,1],[1,0]]  (cycle: 0 needs 1, 1 needs 0)
                #     indegree = [1, 1]  (both need a prereq)
                #     seed: NO course has indegree 0 → q=[] from the start!
                #     while loop never runs → taken = 0
                #     taken(0) == numCourses(2)? NO → return False
                    

        # Why Kahn’s needs no recursion or three-state tracking -> DFS cycle detection needed the THREE-STATE trick (visiting/visited) to detect back-edges along the recursion path. Kahn's sidesteps all that: it's purely iterative (a BFS queue), and "cycle" is detected by the simple count check at the end. No recursion stack, no path tracking, no state array.
                # Advantages of Kahn's over DFS here:
                #     - no recursion depth limit (safe for huge/deep dependency graphs)
                #     - produces a valid ORDERING for free (the order courses are taken) — useful
                #     for Course Schedule II
                #     - the "take what's available" logic is intuitive (mirrors real scheduling)

                # Both are O(V + E); the choice is often style or whether you need the ordering.


        # ----- Edge Cases -----

        # No prerequisites -> All in-degrees are 0 → all courses seeded → all taken → taken == numCourses → True.

        # Self-loop [a, a] -> indegree[a] becomes 1 (a needs itself); a is never in-degree 0 → never taken → taken < numCourses → False.

        # Cycle in a disconnected component -> The acyclic components get fully taken, but the cyclic component’s courses stay stuck → taken < numCourses → False.

        # Everything in one big cycle -> No course starts at in-degree 0 → queue empty from the start → taken = 0 → False.

        # Duplicate prerequisite pairs -> a duplicate [1,0] would increment indegree[1] twice but adj[0] also lists 1 twice, so it’s decremented twice too. It stays consistent and works, but if the problem guaranteed no duplicates you needn’t worry; with duplicates it still balances out correctly.

        # Long chain (no cycle) -> cycle)	Courses unlock one at a time down the chain; all get taken → True. No recursion depth issue (iterative).







