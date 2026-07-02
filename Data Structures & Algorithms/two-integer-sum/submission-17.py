class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        copy = []
        for i, n in enumerate(nums):
            copy.append([n, i])
        
        copy.sort()

        start, end = 0, len(nums) - 1

        while start < end:
            curSum = copy[start][0] + copy[end][0]
            if curSum == target:
                return [min(copy[start][1], copy[end][1]), max(copy[start][1], copy[end][1])]
            elif curSum < target:
                start += 1
            else:
                end -= 1
            