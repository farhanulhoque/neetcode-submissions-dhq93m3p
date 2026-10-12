class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS

        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        state = [0] * numCourses

        result = []

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            state[course] = 2

            result.append(course)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return result