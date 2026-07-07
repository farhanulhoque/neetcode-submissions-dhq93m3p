class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right =  0,  len(heights) - 1
        maxArea = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            currArea = width * height
            maxArea = max(maxArea, currArea)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea

        # TC: O(n) -> Left and right pointers only move inward - combined they traverse at most n steps
        # SC: O(1) -> No data structures used - Just two pointers and a running maximum

        # Solution Description: Place one pointer left at the start and one pointer right at the end. At each step calculate the area formed by the two bars. The width is r - l and the height is limited by the shorter bar — water spills over the shorter one. After recording the area, move the shorter pointer inward. Moving the taller one inward can never increase the area — width always shrinks, and height is already capped by the shorter bar, so the only chance of finding more water is by finding a taller short bar.
        