class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        # Loop through every string in the list and prepend each string with its length and a # separator
        for s in strs:
            result += str(len(s)) + "#" + s
        # Return the fully encoded string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        # i is the main pointer. This tracks where the current chunk starts.
        i = 0
        # Keep going until we've consumed the entire encoded string
        while i < len(s):
            # j starts at i — will scan forward to find the '#'.
            j = i
            # Advance j until we hit # — everything from i to j is the length number.
            while s[j] != "#":
                j += 1
            # Slice s[i:j] to extract the length digits and convert to int
            length = int(s[i:j])
            # move i to first char AFTER the '#' and move j to first digit of the next length number 
            i = j + 1
            j = i + length
            result.append(s[i:j])
            # Jump i forward past this entire chunk to the start of the next one
            i = j
        
        return result


    # TC: O(n) for both -> Encode: Single loop concatenating every character once. Decode: Looks like a nested loop but i and j together never go backwards — they only move forward through the string. Every character is visited exactly once across the entire execution — same reasoning as the bucket sort nested loop
    # SC: O(n) for both -> Encode: The output string holds every original character plus small length prefixes. Decode: The result list holds every original string reconstructed → total characters = n
