class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS directed-cycle detection (with visited set)
        
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        # Set of courses on the current DFS path (the “visiting” state)
        visiting = set()
        
        def dfs(course):
            # If course is already on the current path, we’ve looped back → cycle → return False
            if course in visiting:
                return False
            # If course has no (remaining) prerequisites, it’s finishable → return True (this also catches already-cleared courses)
            if adj[course] == []:
                return True
            
            # Add course to the current path
            visiting.add(course)
            # Explore each of its prerequisites. If any prerequisite leads to a cycle, propagate the failure → return False
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            # Remove course from the current path (backtrack — it’s no longer on the active path)
            visiting.remove(course)
            # Clear course’s prerequisites → marks it fully explored/safe (memoization)
            adj[course] = []

            # Return True — this course is finishable
            return True
        
        # Try every course (the graph may be disconnected). If any course’s DFS finds a cycle, it’s impossible → return False.
        for course in range(numCourses):
            if not dfs(course):
                return False
        # No cycle anywhere → all courses finishable
        return True


        # TC:
            