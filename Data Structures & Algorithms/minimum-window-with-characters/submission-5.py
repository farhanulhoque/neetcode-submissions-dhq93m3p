class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT =  {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        window =  {}
        result = [-1, -1]
        resultLen = float("infinity")
        need, have = len(countT), 0

        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1 
                left += 1
        left, right = result
        return s[left: right + 1] if resultLen != float("infinity") else ""
        