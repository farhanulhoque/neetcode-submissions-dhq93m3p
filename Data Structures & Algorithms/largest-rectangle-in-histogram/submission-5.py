class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # This is to track the max area found
        maxArea = 0
        # Stack of (start_index, height) — where each bar's rectangle could begin
        stack = []

        # Scan each bar with index i and height h
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index) * height)
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        
        return maxArea

        # TC: O(n) -> Each bar is pushed once and popped once. The main loop plus the final leftover loop together touch each bar a constant number of times — amortized O(1) per bar
        # SC: O(n) -> The stack holds up to n bars (e.g. a strictly increasing histogram where nothing is popped until the end)

        # Solution Description: Each bar can form a rectangle that extends left and right until it hits a shorter bar. The largest rectangle using a given bar as its height spans from the first shorter bar on its left to the first shorter bar on its right. We use a monotonic increasing stack of (start_index, height) pairs. As we scan, when the current bar is shorter than the stack top, that taller bar can't extend further right — so we pop it and compute its area, using the popped bar's start index to measure how far left the rectangle reaches. Crucially, when we pop, the current bar can extend back to the popped bar's start index (since everything between was at least as tall). After the scan, any bars remaining on the stack extend all the way to the end.

        # Why not O(n²)? -> The while loop looks nested, but each bar enters and leaves the stack exactly once. Total pops across the whole run ≤ n — the same amortized argument as every monotonic stack problem.
        # 

