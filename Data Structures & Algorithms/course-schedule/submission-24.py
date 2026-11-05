class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        adj = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            adj[crs].append(prereq)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            
            visiting.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)

            adj[course] = []
            
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True