class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # This is to track the max area found
        maxArea = 0
        # Stack of (start_index, height) — where each bar's rectangle could begin
        stack = []

        # Scan each bar with index i and height h
        for i, h in enumerate(heights):
            # start = how far left this bar's rectangle can extend — defaults to its own index
            start = i
            # While the stack top is taller than the current bar, pop it — this taller bar can't extend past the current shorter one
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Compute its area: height × (i - index) — width from its start to here
                maxArea = max(maxArea, (i - index) * height)
                # The current bar can extend back to the popped bar's start (all bars between were ≥ h)
                start = index
            # Push the current bar with its (possibly extended) start index
            stack.append((start, h))
        
        # Bars still on the stack at the end NEVER encountered a shorter bar to their right. They extend all the way to the END of the histogram. Nothing shorter appeared to close them off, their right boundary is the array's end — handled by this final sweep.
        for i, h in stack:
            # Their width extends from their start to the array's end
            maxArea = max(maxArea, (len(heights) - i) * h)
        
        return maxArea

        # TC: O(n) -> Each bar is pushed once and popped once. The main loop plus the final leftover loop together touch each bar a constant number of times — amortized O(1) per bar
        # SC: O(n) -> The stack holds up to n bars (e.g. a strictly increasing histogram where nothing is popped until the end)

        # Solution Description: Each bar can form a rectangle that extends left and right until it hits a shorter bar. The largest rectangle using a given bar as its height spans from the first shorter bar on its left to the first shorter bar on its right. We use a monotonic increasing stack of (start_index, height) pairs. As we scan, when the current bar is shorter than the stack top, that taller bar can't extend further right — so we pop it and compute its area, using the popped bar's start index to measure how far left the rectangle reaches. Crucially, when we pop, the current bar can extend back to the popped bar's start index (since everything between was at least as tall). After the scan, any bars remaining on the stack extend all the way to the end.

        # Why not O(n²)? -> The while loop looks nested, but each bar enters and leaves the stack exactly once. Total pops across the whole run ≤ n — the same amortized argument as every monotonic stack problem.
        # The "start = index" extend-back — When we pop a taller bar, the current bar inherits that bar's start index. Without this, we would miss the wider rectangle it can actually form.
        # When we pop (index, height), the rectangle of THIS height: starts at `index` (where it was pushed / extended back to), ends just before `i` (the current shorter bar blocks it)
        # Why a monotonic increasing stack? -> We pop whenever the top is TALLER than the current bar. So whatever remains is always <= current → stack heights INCREASE bottom to top. This invariant means: for any bar on the stack, everything above it (pushed later) is taller — so when a short bar comes, we resolve the tall bars in the right order (tallest/most-recent first).
        

        