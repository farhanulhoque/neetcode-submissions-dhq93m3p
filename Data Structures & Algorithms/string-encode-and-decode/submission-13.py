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
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        
        return result