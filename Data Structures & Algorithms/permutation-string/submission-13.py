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
        

        # Solution Description: 