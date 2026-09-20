class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        stack = []

        def backtrack(openP, closeP):
            if openP == closeP == n:
                result.append("".join(stack.copy()))
                return

            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closeP)
                stack.pop()
            
            if closeP < openP:
                stack.append(")")
                backtrack(openP, closeP + 1)
                stack.pop()
        
        backtrack(0, 0)
        return result