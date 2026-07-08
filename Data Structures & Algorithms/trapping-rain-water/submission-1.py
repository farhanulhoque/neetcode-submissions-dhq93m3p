class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxL, maxR = height[left], height[right]
        maxArea = 0

        while left < right:
            if maxL <= maxR:
                left += 1
                maxL = max(maxL, height[left])
                maxArea += maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR, height[right])
                maxArea += maxR - height[right]
        
        return  maxArea


        # Solution Description: For every bar, the water it can hold is determined by the shorter of the tallest bars to its left and right, minus its own height. Instead of precomputing prefix/suffix max arrays, we use two pointers with running maximums. At each step, whichever side has the smaller running max is fully determined — we know exactly how much water sits on top of that bar — so we process it and move inward. The side with the larger running max waits because its water level could still be raised by something on the other side.
        
        # Water trapped above any bar = min(tallest bar to its left, tallest bar to its right) - its own height
        # Because we update maxL to include the current bar before computing water, maxL is always at least height[l]. So maxL - height[l] is never negative — you can't have negative water!
        # maxL = "how high is the wall behind me on the left?", maxR = "how high is the wall behind me on the right?",  Water on any bar = shorter wall - my height
        # We always move the side with the smaller running max. If maxL <= maxR, then min(maxL, maxR) = maxL — the left wall is the bottleneck. We already know the water level for the left bar, no matter what happens on the right.
        # Smaller running max = "I know for sure what caps the water here" → safe to process and move
        # Larger running max  = "My water level might still change" → wait, don't process yet
        # We move the shorter wall because its side's water level is locked in — the shorter wall is the bottleneck, and nothing on the other side can lower it further. The taller side stays uncertain until we find out what really limits it.