class Solution:
    def trap(self, height: List[int]) -> int:
        # Initialize left at the start, right at the end
        left, right = 0, len(height) - 1
        # maxL = the tallest bar seen so far from the left side (from index 0 up to left), maxR = the tallest bar seen so far from the right side (from the end back to right)
        maxL, maxR = height[left], height[right]
        # This is to accumulate total trapped water
        maxArea = 0

        while left < right:
            # If Left max is smaller — left side is the bottleneck. The water level is decided by the shorter wall 
            if maxL <= maxR:
                # Move left pointer inward to the next bar
                left += 1
                # Update left running max if this new bar is taller
                maxL = max(maxL, height[left])
                # Water above this bar = maxL - height[l]. Always ≥ 0 because maxL ≥ height[l] by definition. It's the difference between the max left and the current bar that the left pointer is at.
                maxArea += maxL - height[left]
            # Right max is smaller — right side is the bottleneck
            else:
                # Move right pointer inward to the next bar
                right -= 1
                # Update right running max if this new bar is taller
                maxR = max(maxR, height[right])
                # Water above this bar = maxR - height[r]. Always ≥ 0 because maxR ≥ height[r]
                maxArea += maxR - height[right]
        # Return total trapped water. The area was added in every iteration
        return  maxArea

        # TC: O(n) -> left and right pointers only move inward — combined they traverse exactly n steps
        # SC: O(1) -> Just two pointers and two running maximums — no extra data structures used

        # Solution Description: For every bar, the water it can hold is determined by the shorter of the tallest bars to its left and right, minus its own height. Instead of precomputing prefix/suffix max arrays, we use two pointers with running maximums. At each step, whichever side has the smaller running max is fully determined — we know exactly how much water sits on top of that bar — so we process it and move inward. The side with the larger running max waits because its water level could still be raised by something on the other side.
        
        # Water trapped above any bar = min(tallest bar to its left, tallest bar to its right) - its own height
        # Because we update maxL to include the current bar before computing water, maxL is always at least height[l]. So maxL - height[l] is never negative — you can't have negative water!
        # maxL = "how high is the wall behind me on the left?", maxR = "how high is the wall behind me on the right?",  Water on any bar = shorter wall - my height
        # We always move the side with the smaller running max. If maxL <= maxR, then min(maxL, maxR) = maxL — the left wall is the bottleneck. We already know the water level for the left bar, no matter what happens on the right.
        # Smaller running max = "I know for sure what caps the water here" → safe to process and move
        # Larger running max  = "My water level might still change" → wait, don't process yet
        # We move the shorter wall because its side's water level is locked in — the shorter wall is the bottleneck, and nothing on the other side can lower it further. The taller side stays uncertain until we find out what really limits it.
