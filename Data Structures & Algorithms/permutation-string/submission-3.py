class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        countS1 = {}
        for char in s1:
            countS1[char] = countS1.get(char, 0) + 1
        
        need = len(countS1)
        for i in range(len(s2)):
            countS2 = {}
            match = 0
            for j in range(i, len(s2)):
                countS2[s2[j]] = countS2.get(s2[j], 0) + 1
                if countS1.get(s2[j], 0) < countS2[s2[j]]:
                    break
                if countS1.get(s2[j], 0) == countS2[s2[j]]:
                    match += 1
                if need == match:
                    return True
        
        return False
                    