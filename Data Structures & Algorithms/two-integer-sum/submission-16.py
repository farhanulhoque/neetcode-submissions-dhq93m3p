class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store {number: index}
        numMap = {}

        for i, n in enumerate(nums):
            # Calculate the complement — the number we'd need to pair with num to hit target
            diff = target - n
            # Check if that complement was already seen earlier. If yes — we found our pair! Return [smaller_index, i]. Since numMap[diff] was stored before i, it's always the smaller index first 
            if diff in numMap:
                return [numMap[diff], i]
            # If not found yet, store this number and its index
            numMap[n] = i

            # TC: O(n) -> Single pass through the array
            # SC: O(n) -> The hashmap can grow up to n entries

        