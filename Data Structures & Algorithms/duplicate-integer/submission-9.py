class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        visited = set()

        for n in nums:
            if n in visited:
                return True
            else:
                visited.add(n)
        
        return False

        # TC: O(n)
        # SC: O(n)