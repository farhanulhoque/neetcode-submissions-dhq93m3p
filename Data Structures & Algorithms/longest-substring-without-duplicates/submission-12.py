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
            # It stores (or updates) the character's latest position in the dictionary. Repeated characters overwrite their old index with the new one. The map always holds the most recent position of each character.
            charMap[s[right]] = right
            # Record the current window size
            longest = max(longest, right - left + 1)
        
        return longest

        # TC: O(n) -> Single pass — r moves through once, l only jumps forward
        # SC: O(min(m, n)) ->  Map holds at most m distinct characters


        # Set version: when we hit a duplicate, we shrink l one step at a time until the duplicate is gone.
        # HashMap version: when we hit a duplicate, we jump l directly past the previous occurrence in one move.
        
        # The whole HashMap optimization depends on knowing where a duplicate last appeared, so we can jump left past it
        # Without constantly updating charMap[s[right]] = right, the next time we see this character we'd be jumping to a stale, outdated position. If we updated the map before the check, we'd overwrite the old index and lose the information we needed to make the jump decision. Always read first, then update.
        # charMap[s[right]] >= left → is that previous sighting inside the current window? A character can be in the map but sit to the left of our window — meaning it's already been left behind and is not a real duplicate anymore. This guards against the left pointer moving backward when a duplicate is outside the current window
        # charMap stores every character we've ever seen — it doesn't automatically delete characters when they fall out of the window. So the map can contain stale indices pointing to positions that are no longer inside [left...right]. The >= left check filters those out.