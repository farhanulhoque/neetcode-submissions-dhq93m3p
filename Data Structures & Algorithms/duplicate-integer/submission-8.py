class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numSet = set()

        for n in nums:
            if n not in numSet:
                numSet.add(n)
            else:
                return True
        
        return False