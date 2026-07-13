class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Output list — this is to store one max value per window
        result = []
        # Deque storing indices (not values), kept in decreasing value order. Only an INDEX tells us its position → whether l > q[0]. A raw value gives us no position information.
        q = deque()

        # Initialize left pointer
        left = 0
        # right pointer expands rightward through the array
        for right in range(len(nums)):
            # While the deque's back holds a value smaller than the incoming one, Pop it — it can never be a max again. Using < keeps equal elements in the deque, which is safe. Both actually produce correct maxes here, but < avoids discarding equal-valued elements that might still be needed for later windows.
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            # Add the current index to the back of the queue
            q.append(right)

            # If the front index has fallen outside the window's left bound, remove it from the front. We only evict when l has moved PAST q[0], not when it equals it, hence we use > instead of >=
            if left > q[0]:
                q.popleft()
            
            # Once we've seen at least k elements, a full window exists. right is 0-indexed, so after processing index right we've seen (right + 1) elements. We can only form a full window once we've seen k elements. r + 1 keeps growing as r marches to the end of the array. The window size stays fixed at k because left advances alongside right. This check asks "Have we seen enough elements yet to have formed our first complete window?". Once that's true (at r = k-1), it stays true forever after — because r + 1 only grows. That's exactly why we use >=: every subsequent iteration also has a full window ready to record.
            if right + 1 >= k:
                # The front of the deque is the current window's max — record it
                result.append(nums[q[0]])
                # Slide the left pointer forward
                left += 1
        
        return result

        # TC: O(n) -> Each index is added once and removed once from the deque across the entire run. Even though there's a while loop, the total pops over all iterations is at most n — average O(1) per element. each element enters and exits the deque exactly once. Total work across all iterations is 2n
        # SC: O(k) -> The deque holds at most k indices at any time (the current window's candidates)

        # Solution Description: Use a monotonic deque that stores indices whose values are in decreasing order. The front of the deque always holds the index of the current window's maximum. For each new element: pop from the back while the incoming value is larger (those smaller values can never be the max again), then add the new index. Pop from the front if it has slid out of the window's left bound. Once the first full window is formed, the front of the deque is the max — record it.

        # The key insight: a smaller element that appears before a larger one is useless — it can never be the maximum of any future window that also contains the larger one. So we discard it.
        # Why store indices, not values? -> We must know if the max has slid out of the window. Only an INDEX tells us its position → whether l > q[0]. A raw value gives us no position information. If we stored values, two 5's are indistinguishable. Indices keep them distinct so we can track which one is in-window.
        # Any future window containing the smaller element ALSO contains the larger one (it came later and is still in range). So the larger one always "beats" it → smaller is useless → discard.
        # The deque stays monotonically decreasing in value from front to back.
        # r + 1 is NOT the window size — it's the count of elements seen so far.
        # r + 1 climbs 1, 2, 3, 4, 5... but the window size holds steady at 3. That's because every time r steps right, l also steps right (once we're past the first window).
