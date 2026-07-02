class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Create an empty dictionary to track character frequencies
        count = {}

        # count characters in s and store in the freqency map
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Decrement character's count for each char in t 
        for char in t:
            count[char] = count.get(char, 0) - 1
            # if any count goes negative, t has a char s doesn't have. 
            if count[char] < 0:
                return False
        
        # All counts balanced out. Return true.
        return True

        # TC: O(n) -> Two linear passes over strings of length n
        # SC: O(1) -> At most 26 keys in the map (lowercase letters) — constant space.


        # The array version is faster in practice due to direct index access vs hashing, but the dictionary version is more flexible for unicode inputs.

        