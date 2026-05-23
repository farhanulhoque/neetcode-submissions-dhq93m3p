class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if len(s) != len(t):
        #     return False

        # sCount = {}
        # tCount = {}

        # for i in range(len(s)):
        #     sCount[s[i]] = sCount.get(s[i], 0) + 1
        #     tCount[t[i]] = tCount.get(t[i], 0) + 1
        
        # return sCount == tCount

        # # TC: O(n + m), where n is the length of s and m is the length t 
        # # SC: O(1), since we have at most 26 different characters





        if len(s) != len(t):
            return False

        count = [0] * 26
        
        for i in range(len(s)):
            # ord(s[i]) - ord('a') converts a letter to an index (a=0, b=1, ... z=25), then increments that slot for s
            count[ord(s[i]) - ord('a')] += 1
            # Same index trick, but decrements that slot for t 
            count[ord(t[i]) - ord('a')] -= 1
        
        for n in count:
            if n != 0:
                return False
        
        # If every slot is 0, all characters balanced out perfectly
        return True

        # This approach is slightly more memory-efficient. Instead of a dictionary, you use a fixed-size array of 26 integers (one slot for each letter).
        # The Key Trick — ord() Mapping
        # So the array acts like a manual hash table where the character itself is the hash key, mapped to a fixed position.
