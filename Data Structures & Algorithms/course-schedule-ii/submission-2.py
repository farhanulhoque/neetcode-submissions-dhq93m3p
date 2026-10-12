class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn’s Algorithm (BFS Topological Sort)

        # Adjacency list keyed by prerequisite: adj[pre] = courses that depend on pre
        adj = {i: [] for i in range(numCourses)}
        # indegree[c] = how many prerequisites course c still needs
        indegree = [0] * numCourses

        # For each pair [crs, pre] (crs needs pre)
        for crs, pre in prerequisites:
            # add edge pre → crs (taking pre unlocks crs)
            adj[pre].append(crs)
            # increment crs’s in-degree
            indegree[crs] += 1
        
        # The BFS queue
        q = deque()
        # Scan every course
        for crs in range(numCourses):
            # if it has no prerequisites (in-degree 0), seed the queue with it
            if indegree[crs] == 0:
                q.append(crs)
        
        # The result — the topological order we build up
        result = []

        # Process until no takeable courses remain
        while q:
            # Take the next available course (dequeue)
            course = q.popleft()
            # Append it to the result list (maintaining order)
            result.append(course)
            
            # For each course that depended on this one
            for nxt in adj[course]:
                # one prerequisite is now satisfied → decrement its in-degree
                indegree[nxt] -= 1
                # If that dependent now has zero remaining prerequisites, it’s newly takeable → enqueue it
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        # If we ordered all courses → return the result; else a cycle exists → return []
        return result if len(result) == numCourses else []


        # TC: O(V + E) -> building adj + in-degrees: O(V + E). Seeding: O(V). BFS: each course dequeued once (O(V) dequeues), each edge processed once (the decrements) → O(V + E). O(V + E) overall.
        # SC: O(V + E) -> adjacency list: O(V + E). in-degree array: O(V). queue: up to O(V). the order list: O(V) (the output). O(V + E) total.

        # V = numCourses, E = prerequisites.


        # Solution Description: This is Course Schedule I, but instead of returning True/False, we return an actual topological ordering — a sequence where each course appears after all its prerequisites. If a cycle exists, no such ordering is possible, so we return []. With Kahn’s algorithm, the order falls out naturally: we take courses with no remaining prerequisites (in-degree 0), appending each to the result as we take it. Taking a course decrements its dependents’ in-degrees, unlocking more courses. The sequence in which courses leave the queue is a valid topological order. At the end, if we ordered all numCourses, return the order; if fewer (some stuck in a cycle), return [].


        # ----- Deep Dive -----

        # Why the dequeue order IS a valid topological order -> A course is only enqueued when its in-degree hits 0 — meaning ALL its prerequisites have already been taken (and thus already appended to `order`). So when we append a course, every prerequisite it needs is ALREADY in `order`, earlier in the sequence. That's EXACTLY the definition of a topological order: each course comes after all its prerequisites. We get the ordering for FREE — no sorting, no extra passes. The queue's natural processing order respects all dependencies.
                # course enqueued ⟺ all prereqs taken ⟺ all prereqs already in order → appending it now places it AFTER its prereqs → valid ordering. 
        

        # Why len(order) == numCourses guards against cycles -> Same cycle-detection logic as Course Schedule I, repurposed to return the right thing:
                # no cycle → every course gets taken → len(order) == numCourses → return order.
                # cycle    → cyclic courses never reach in-degree 0 → never taken → never appended → len(order) < numCourses → return [] (impossible).

                # The problem demands an EMPTY array when it's impossible, so we check the length and return [] if a cycle left some courses out. Cyclic courses are stuck waiting on each other forever → excluded from order → the length falls short → we correctly report impossibility.
        

        # Why multiple valid orderings exist (and that’s fine) -> When MULTIPLE courses have in-degree 0 at the same time, ANY of them can be taken next — they don't depend on each other. The queue's FIFO order picks one sequence, but other orders would be equally valid. The problem accepts ANY valid order, so the FIFO choice is fine. (Using a different queue/stack would give a different — still valid — order.)


        # ----- Edge Cases -----

        # No prerequisites -> 	All in-degrees 0 → all seeded → order = [0, 1, ..., numCourses-1] (any order valid). Returns a full ordering.

        # Single course -> In-degree 0 → taken → order = [0].

        # Self loop [a, a] -> indegree[a] ≥ 1, never 0 → a never taken → short order → [].

        # Duplicate pairs -> In-degrees increment and decrement consistently → still works (worth clarifying if duplicates are possible).

        # Cycle (Whole graph) -> No in-degree-0 course → queue empty → order = [] → len(order) != numCourses → return [].

        # Partial cycle -> Acyclic part gets ordered, cyclic part stuck → len(order) < numCourses → return [] (even the orderable part is discarded, as required).

        # Disconnected (no prereqs between groups) -> All independent courses seeded → all ordered → valid full ordering.







        
        