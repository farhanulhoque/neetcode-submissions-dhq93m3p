class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False

        # Solution Description: Brackets must close in last-in-first-out order — the most recently opened bracket is the one that must close next. That's exactly what a stack models. Push every opening bracket onto the stack. When a closing bracket appears, check whether the top of the stack is its matching opener: if yes, pop it; if no (or the stack is empty), the string is invalid. At the end, a truly valid string leaves the stack empty — every opener was matched. A leftover opener means something never closed.

        # This is the canonical stack use case: LIFO matching. The pattern is "push things you're waiting to resolve, pop when they're resolved."
