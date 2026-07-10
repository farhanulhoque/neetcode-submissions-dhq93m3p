class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        
        need = len(count1)
        for i in range(len(s2)):
            count2 = {}
            match = 0
            for j in range(i, len(s2)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    match += 1
                if match == need:
                    return True
        
        return False
                    