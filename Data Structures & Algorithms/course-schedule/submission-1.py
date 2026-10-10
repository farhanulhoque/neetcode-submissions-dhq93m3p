class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS directed-cycle detection (3 state)

        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
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
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True