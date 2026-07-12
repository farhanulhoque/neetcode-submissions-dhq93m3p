class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        q = deque()

        left = 0
        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()
            
            if right + 1 >= k:
                result.append(nums[q[0]])
                left += 1
        
        return result

        # TC: O(n) -> Each index is added once and removed once from the deque across the entire run. Even though there's a while loop, the total pops over all iterations is at most n — average O(1) per element
        # SC: O(k) -> The deque holds at most k indices at any time (the current window's candidates)