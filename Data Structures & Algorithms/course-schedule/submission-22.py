class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        state = [0] * numCourses

        def dfs(crs):
            if state[crs] == 1:
                return False
            
            if state[crs] == 2:
                return True
            
            state[crs] = 1
            for prereq in adj[crs]:
                if not dfs(prereq):
                    return False
            state[crs] = 2

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True