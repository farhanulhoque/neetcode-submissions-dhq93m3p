class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []

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

        # Solution Description: Each bar can form a rectangle that extends left and right until it hits a shorter bar. The largest rectangle using a given bar as its height spans from the first shorter bar on its left to the first shorter bar on its right. We use a monotonic increasing stack of (start_index, height) pairs. As we scan, when the current bar is shorter than the stack top, that taller bar can't extend further right — so we pop it and compute its area, using the popped bar's start index to measure how far left the rectangle reaches. Crucially, when we pop, the current bar can extend back to the popped bar's start index (since everything between was at least as tall). After the scan, any bars remaining on the stack extend all the way to the end.

