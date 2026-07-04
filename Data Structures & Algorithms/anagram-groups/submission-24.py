class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for word in strs:
            sortedS = ''.join(sorted(word))
            result[sortedS].append(word)
        
        return list(result.values())