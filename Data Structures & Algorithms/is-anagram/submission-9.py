class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sCount = {}
        tCount = {}

        for i in range(len(s)):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            tCount[t[i]] = tCount.get(t[i], 0) + 1
        
        return sCount == tCount

        # TC: O(n + m), where n is the length of s and m is the length t 
        # SC: O(1), since we have at most 26 different characters


        


        