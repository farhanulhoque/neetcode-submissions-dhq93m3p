class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        if s1Count == s2Count:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            s2Count[ord(s2[right]) - ord('a')] += 1
            s2Count[ord(s2[left]) - ord('a')] -= 1

            left += 1

            if s1Count ==  s2Count:
                return True
        return False

        # TC: O(n) -> n slides, each doing a 26-element comparison. 26 is a constant, so it reduces to O(n)
        # SC: O(1) -> Two fixed arrays of 26 characters
        

        # Solution Description: A permutation of s1 is an anagram — same character counts, any order. Build a 26-slot frequency array for s1, then slide a fixed-size window of length len(s1) across s2, keeping a matching count array for the window. Each slide increments the entering character and decrements the leaving one. After each slide, compare the two arrays — if all 26 counts match, it's a permutation. Arrays compare position by position, so leftover zeros are harmless.
