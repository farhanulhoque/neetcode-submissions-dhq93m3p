class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) - 1

        while left < right:
            curSum = numbers[left] + numbers[right]
            # if curSum is too small — we need a bigger number
            if curSum < target:
                left += 1
            # if curSum is too large — we need a smaller number
            elif curSum > target:
                right -= 1
            else:
                # Return 1-indexed positions by adding 1 to both pointers
                return [left + 1, right + 1]
        
        # TC: O(n) -> Each pointer only moves inward - combined they traverse at most n steps
        # SC: O(1) -> No data structures used. Just two integer pointers.

        # Solution Descrition: Place one pointer l at the start and one pointer r at the end of the array. At each step compute the sum of the two pointed elements. If the sum equals target we are done. If the sum is too small, move l rightward to increase it. If the sum is too large, move r leftward to decrease it. This works because the array is sorted — moving pointers in either direction has a predictable effect on the sum.
        