class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS Topological Sort (Kahn's Algorithm)

        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        taken = 0

        while q:
            course = q.popleft()
            taken += 1

            for nxt in adj[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return taken == numCourses
        
        # TC: 
        # TC:


        # Solution Description: Instead of DFS cycle detection, Kahn’s algorithm builds a valid ordering and checks whether it covers all courses. Each course has an in-degree = the number of prerequisites it still needs. Courses with in-degree 0 can be taken immediately. We seed a queue with all in-degree-0 courses. Repeatedly: take one (dequeue it, count it), and for each course that depended on it, decrement that course’s in-degree (one prerequisite satisfied). If a dependent’s in-degree drops to 0, it’s now takeable → enqueue it. Continue until the queue empties. If we took all numCourses, there’s no cycle (finishable); if some courses were never takeable (stuck with in-degree > 0 — trapped in a cycle), we took fewer than numCourses → not finishable.


        # ----- Deep Dive -----

        # 


        # ----- Edge Cases -----

        # 







