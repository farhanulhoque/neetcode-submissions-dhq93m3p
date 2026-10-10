class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS directed-cycle detection (with visited set)

        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False
            if adj[course] == []:
                return True
            
            visiting.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            adj[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
            