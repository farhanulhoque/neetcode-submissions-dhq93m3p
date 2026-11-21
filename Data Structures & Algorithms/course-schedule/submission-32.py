class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            adj[crs].append(prereq)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if adj[crs] == []:
                return True
            
            visiting.add(crs)
            for prereq in adj[crs]:
                if not dfs(prereq):
                    return False
            visiting.remove(crs)
            
            adj[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True