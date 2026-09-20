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

        
        # TC: 
        # SC: 


        # Solution Description: Unlike the previous problems (which picked elements from an array), here each step chooses one of two characters: ( or ). The art is knowing when each is allowed, so we only ever build valid strings. Two rules govern the choices, tracked by counts of open and close parentheses used so far: 1. We can add ( as long as we haven't used all n opens (open < n). 2. We can add ) only if it would have a matching open before it (close < open). We build the string character by character, applying these rules to decide which additions are legal. When the string reaches length 2n (all n pairs placed), it's a complete valid string. The constraints prune invalid paths before we explore them — so we never generate a malformed string in the first place.


        # ----- Deep Dive -----

        # 







