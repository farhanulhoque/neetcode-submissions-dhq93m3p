class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)

        indegree = [0] * numCourses

        for crs, prereq in prerequisites:
            adj[prereq].append(crs)
            indegree[crs] += 1

        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        result = []

        while q:
            course = q.popleft()

            result.append(course)

            for nxt in adj[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return result if len(result) == numCourses else []

