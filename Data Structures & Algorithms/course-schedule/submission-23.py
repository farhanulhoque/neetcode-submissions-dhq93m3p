class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            adj[crs].append(prereq)
        
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            state[course] = 2

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True