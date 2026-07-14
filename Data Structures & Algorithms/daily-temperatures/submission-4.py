class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # This is the result array pre-filled with 0 (the default for days with no warmer future)
        result = [0] * len(temperatures)
        # This Stack is for holding indices of days awaiting a warmer temperature
        stack = []

        # Scan each day with its index i and temperature temp
        for i, temp in enumerate(temperatures):
            # While the stack is non-empty and today is warmer than the day on top of stack, pop that waiting day's index
            while stack and temp > temperatures[stack[-1]]:
                prevIndex = stack.pop()
                # Its answer is the gap: i - prevIndex days until warmer
                result[prevIndex] =  i - prevIndex
            stack.append(i)
        
        return result
        

        # Solution Description: For each day we want the distance to the next warmer day. This is the classic "next greater element" problem, solved with a monotonic decreasing stack of indices. We scan left to right, keeping a stack of days that are still waiting for a warmer temperature. When the current day is warmer than the day at the top of the stack, we've found that day's answer — pop it and record the day gap (current index - popped index). We keep popping while the current day is warmer than the stack's top, since one warm day can resolve multiple waiting days. Days that never get a warmer future day stay at 0 (the default).

        # Next Greater Element -> The canonical use of a monotonic stack
        # Monotonic Stack (decreasing) -> Stack holds indices of days still waiting for a warmer day

