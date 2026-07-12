class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""
        
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        window = {}
        result = [-1, -1]
        resultLen =  float("infinity")
        have, need = 0, len(countT)

        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                if (right - left + 1) < resultLen:
                    result =  [left, right]
                    resultLen = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        
        left, right = result
        return s[left: right + 1] if resultLen != float("infinity") else ""

        # TC: O(n + m) -> m = len(t) to build countT. Then n = len(s): right traverses once, left traverses once — each character enters and leaves the window at most once
        # SC: O(m) -> countT and window hold at most m distinct characters (or bounded by alphabet size)

        # Solution Description: We need the smallest window in s containing every character of t (with duplicates). Track a need map of required counts and a have counter of how many requirements are currently met. Expand the window with r, and each time a character reaches its required count, increment have. Once have == need (all requirements met), the window is valid — now shrink from the left as far as possible while staying valid, recording the smallest valid window seen. This grow-then-shrink is the key difference from earlier sliding window problems: we shrink while the window is still valid to minimize its size.
