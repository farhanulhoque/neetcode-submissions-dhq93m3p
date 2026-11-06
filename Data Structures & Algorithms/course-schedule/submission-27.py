class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        adj = {i: [] for i in range(numCourses)}

        indegree = [0] * numCourses

        for crs, prereq in prerequisites:
            adj[prereq].append(crs)
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
                    