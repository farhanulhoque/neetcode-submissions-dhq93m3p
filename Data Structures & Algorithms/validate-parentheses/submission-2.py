class Solution:
    def isValid(self, s: str) -> bool:
        # This Stack is to hold unmatched opening brackets
        stack = []
        # Map each closing bracket to its matching opening bracket
        closeToOpen = {")": "(", "}": "{", "]": "["}

        # Scan each character in s
        for char in s:
            # Check if the current char is a closing bracket (keys of the map are closers)
            if char in closeToOpen:
                # If the Stack sis non-empty AND its top is the matching opener, Match found — pop the opener off
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                # No match (wrong type or empty stack) → invalid
                else:
                    return False
            # It's an opening bracket → push it into the stack
            else:
                stack.append(char)
        
        # Valid only if the stack is empty — every opener got matched. An opener-without-closer fails.
        return True if not stack else False

        # TC: O(n) -> Single pass through the string; each push/pop is O(1)
        # SC: O(n) -> Worst case all openers (e.g. "(((((") → stack holds up to n characters

        # Solution Description: Brackets must close in last-in-first-out order — the most recently opened bracket is the one that must close next. That's exactly what a stack models. Push every opening bracket onto the stack. When a closing bracket appears, check whether the top of the stack is its matching opener: if yes, pop it; if no (or the stack is empty), the string is invalid. At the end, a truly valid string leaves the stack empty — every opener was matched. A leftover opener means something never closed.

        # This is the canonical stack use case: LIFO matching. The pattern is "push things you're waiting to resolve, pop when they're resolved."
        # The stack and ... part must come first. This is short-circuit protection. If you wrote stack[-1] == closeToOpen[c] and stack, it would crash on the very first closing bracket with an empty stack. Order is not optional here.
        # A closer-without-opener fails inside the loop; an opener-without-closer fails at the final check. You need both to be fully correct.
        # Why map closers→openers and not openers→closers? -> When we see a CLOSER, we need to know what OPENER should be on the stack. closer ')' → expect '(' on top → closeToOpen[')'] gives us '('
        