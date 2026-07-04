class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            result[tuple(count)].append(word)
        
        return list(result.values())

        # TC: O(n * k) -> Total work is n words × k characters each. Every other operation inside the loop — building the tuple, appending to the dict — is O(26) which is constant, so it doesn't affect the complexity.
        # SC: O(n * k) -> Stores all n words, each of length up to k