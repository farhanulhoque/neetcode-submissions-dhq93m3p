class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            i = ord(s2[right]) - ord('a')
            s2Count[i] += 1
            if s1Count[i] == s2Count[i]:
                matches += 1
            elif s1Count[i] + 1 == s2Count[i]:
                matches -= 1

            i = ord(s2[left]) - ord('a')
            s2Count[i] -= 1
            if s1Count[i] == s2Count[i]:
                matches += 1
            elif s1Count[i] - 1 == s2Count[i]:
                matches -= 1
            
            left += 1
        
        return matches == 26
        
        # Solution Description:A permutation of s1 is just an anagram of s1 — same character counts, any order. So we slide a window of exactly len(s1) across s2 and check whether the window's character counts match s1's. The naive check compares all 26 counts each step. The optimization: maintain a matches counter tracking how many of the 26 letters currently have equal counts. When a character enters or leaves the window, only that one letter's bucket changes — so we adjust matches by ±1 instead of rescanning all 26. When matches == 26, we've found a permutation.
                    