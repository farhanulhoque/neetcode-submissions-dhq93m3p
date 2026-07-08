class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary mapping each character to its most recent index
        charMap = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            # If s[right] was seen before AND that occurrence is inside the current window (>= left)
            if s[right] in charMap and charMap[s[right]] >= left:
                # Shift "left" to just past the previous occurrence — instantly removing the duplicate
                left = charMap[s[right]] + 1
            # Update this character's latest index to right
            charMap[s[right]] = right
            # Record the current window size
            longest = max(longest, right - left + 1)
        
        return longest


        # Set version: when we hit a duplicate, we shrink l one step at a time until the duplicate is gone.
        # HashMap version: when we hit a duplicate, we jump l directly past the previous occurrence in one move.
