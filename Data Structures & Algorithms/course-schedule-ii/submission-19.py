class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i: [] for i in range(numCourses)}

        for crs, prereq in prerequisites:
            adj[crs].append(prereq)
        
        state = [0] * numCourses

        result = []

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

            result.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return result
