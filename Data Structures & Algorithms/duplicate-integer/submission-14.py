class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        visited = set()

        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        
        return False

        # TC: O(n) -> You go through the array once. set lookups and set insert are O(1) average, so doing that for n numbers gives O(n) total time.
        # SC: O(n) -> In the worst case, there are no duplicates, so the set stores every number. That means the set can grow to size n.