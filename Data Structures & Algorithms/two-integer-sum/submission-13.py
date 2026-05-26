class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # numMap = {}

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in numMap:
        #         # Since numMap[diff] was stored before i, it's always the smaller index first
        #         return [numMap[diff], i]
        #     # If not found yet, store this number and its index for future lookups
        #     numMap[n] = i
        
        # # TC: O(n), Single pass through the array
        # # SC: O(n), numMap dict can grow up to n entries

        numsCopy = []

        for i, num in enumerate(nums):
            numsCopy.append([num, i])

        numsCopy.sort()

        p1, p2 = 0, len(nums) - 1

        while p1 < p2:
            curSum = numsCopy[p1][0] + numsCopy[p2][0]
            if curSum == target:
                return [min(numsCopy[p1][1], numsCopy[p2][1]), max(numsCopy[p1][1], numsCopy[p2][1])]
            elif curSum < target:
                p1 += 1
            else:
                p2 -= 1
                

        
