class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Create a dictionary where missing keys auto-initialize to an empty list
        result = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for char in str:
                # Increment the slot for this character using the ord() index trick
                count[ord(char) - ord('a')] += 1
            # Convert the count array to a tuple (so it's hashable as a dict key), then append the word to its group
            result[tuple(count)].append(str)
        
        # Return all grouped lists — the values of our dictionary
        return list(result.values())

        # TC: O(m * n), where m is the number of strings in strs and n is the length of the longest string
        # SC: O(m * n), stroing all words across all groups

        # All anagrams will produce the exact same character count array, so we can use that array as a shared dictionary key to group them

