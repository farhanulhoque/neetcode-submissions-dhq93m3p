class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            if s[right] in charMap and charMap[s[right]] >= left:
                left = charMap[s[right]] + 1
            charMap[s[right]] = right
            longest = max(longest, right - left + 1)
        
        return longest
