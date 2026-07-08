class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize left at the start, right at the end — maximum possible width
        left, right =  0,  len(heights) - 1
        # This is to track the best area seen so far
        maxArea = 0

        while left < right:
            # Width is the distance between the two bars
            width = right - left
            # Height is capped by the shorter bar — water spills over it
            height = min(heights[left], heights[right])
            currArea = width * height
            # Update max area if current one is larger
            maxArea = max(maxArea, currArea)

            # Check which bar is shorter. Move the pointer on the shorter bar inward
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea

        # TC: O(n) -> Left and right pointers only move inward - combined they traverse at most n steps
        # SC: O(1) -> No data structures used - Just two pointers and a running maximum

        # Solution Description: Place one pointer left at the start and one pointer right at the end. At each step calculate the area formed by the two bars. The width is r - l and the height is limited by the shorter bar — water spills over the shorter one. After recording the area, move the shorter pointer inward. Moving the taller one inward can never increase the area — width always shrinks, and height is already capped by the shorter bar, so the only chance of finding more water is by finding a taller short bar.
        
        # This greedy choice — always move the shorter pointer — is what makes two pointers provably correct here. We never skip a potentially better answer because moving the taller bar inward mathematically cannot improve the area.
