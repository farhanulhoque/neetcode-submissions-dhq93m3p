class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for n in count:
            if n != 0:
                return False
        
        return True

        # This is efficient because it uses hashing and uses constant space

        # TC: O(n + m)
        # SC: O(1) -> Always exactly 26 integers — truly fixed