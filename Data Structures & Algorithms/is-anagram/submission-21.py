class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        return sMap == tMap


        # TC: O(n + m) -> Two linear passes over the strings
        # SC: O(1) -> We have at most 26 different characters. If the input were unicode, it'd be O(k) where k is the number of unique characters.
        
        # The dictionary version is more flexible for unicode inputs.