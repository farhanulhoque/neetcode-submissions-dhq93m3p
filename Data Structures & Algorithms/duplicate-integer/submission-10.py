class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsSet = set()

        for n in nums:
            if n in numsSet:
                return True
            numsSet.add(n)
        
        return False