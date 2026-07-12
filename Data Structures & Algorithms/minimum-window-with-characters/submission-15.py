class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Empty t → nothing to match → return empty string
        if t == "":
            return ""
        
        # Build countT — how many of each character t requires
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        # window tracks character counts in the current window
        window = {}
        # have = requirements currently met; need = total distinct chars required
        have, need = 0, len(countT)
        # result stores best window's [left, right] indices; resultLen tracks its length (start at infinity)
        result, resultLen = [-1, -1], float("infinity")
        
        # Initialize left pointer
        left = 0
        # right pointer expands the window rightward
        for right in range(len(s)):
            # Add the new character to the window count
            window[s[right]] = window.get(s[right], 0) + 1

            # If this character just reached its required count, one more requirement is satisfied
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1

            # While all requirements are met — window is valid
            while have == need:
                # If this window is smaller than the best so far, record it
                if (right - left + 1) < resultLen:
                    result =  [left, right]
                    resultLen = right - left + 1
                # Shrink: decrement the leftmost character's count. The "in countT" check ensures we only react to characters that actually matter. Without it, the guard short-circuits — Python checks c in countT first, and if it's False, it never evaluates the window[c] == countT[c] part.
                window[s[left]] -= 1
                # If dropping it broke a requirement (count fell below required), have -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                # Move left pointer rightward
                left += 1
        
        # Unpack the best window's bounds
        left, right = result
        # Return the substring, or "" if no valid window was ever found
        return s[left: right + 1] if resultLen != float("infinity") else ""

        # TC: O(n + m) -> m = len(t) to build countT. Then n = len(s): right traverses once, left traverses once — each character enters and leaves the window at most once
        # SC: O(m) -> countT and window hold at most m distinct characters (or bounded by alphabet size)

        # Solution Description: We need the smallest window in s containing every character of t (with duplicates). Track a need map of required counts and a have counter of how many requirements are currently met. Expand the window with r, and each time a character reaches its required count, increment have. Once have == need (all requirements met), the window is valid — now shrink from the left as far as possible while staying valid, recording the smallest valid window seen. This grow-then-shrink is the key difference from earlier sliding window problems: we shrink while the window is still valid to minimize its size.

        # The whole point is to update have incrementally — nudging it by ±1 as characters enter and leave — so we never rescan. But that only works if we update it at the right moments. The in countT check ensures we only react to characters that actually matter. So the first job of c in countT is simply to avoid a crash on characters we don't care about. have must only move for characters that are genuine requirements. The in countT check enforces that.
        # The in countT guards are what let have/need stay O(1). Without them you'd either crash on unrelated characters or corrupt the counter — forcing you back to the slower full-map comparison.
        