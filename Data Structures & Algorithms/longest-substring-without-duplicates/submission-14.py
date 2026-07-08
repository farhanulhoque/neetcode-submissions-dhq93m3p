class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # This set is to track characters currently in the window
        charSet  = set()
        # This marks the left edge of the window
        left = 0
        # This is to track the longest valid window length
        longest = 0

        # right expands the window one character at a time
        for right in range(len(s)):
            # While the new character already exists in the window, remove the leftmost character from the set and shrink the window from the left
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1    
            # add the new character to the set — window has no duplicates 
            charSet.add(s[right])
            # Window size is right - left + 1 — update the maximum. Because both endpoints are included, subtracting alone undercounts by one. r - l + 1 gives the number of elements in the window from index l to index r inclusive.
            longest =  max(longest, right - left + 1)

        return longest

        # TC: O(n) -> Each character is added once and removed at most once — l and r each traverse the string at most once. Total 2n = O(n)
        # SC: O(n) -> The set holds at most min(n, m) characters, where m is the size of the character set

        # Solution Description: Slide a window across the string with two pointers l and r. Expand the window by moving r rightward, adding each new character to a set. If the new character is already in the set, we have a duplicate — shrink the window from the left by removing s[l] and moving l rightward until the duplicate is gone. After each valid expansion, record the window size. The set always represents exactly the characters currently inside the window, so a clean set means no duplicates.
        
        #  Why not O(n²) despite the nested while loop? -> l only ever moves forward across the entire run, never resetting. Across the whole execution, l advances at most n times total, so the inner while loop shares a budget of n — not n per outer iteration.
        # window size is always r - l + 1 when both pointers sit on elements in the window.
        # The set must always mirror exactly what's inside the current window — no more, no less.
        # Every time left advances, the character it leaves behind is removed from the set. This keeps the set perfectly synced with the window
