class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Heapify-all, shrink

        # Use nums directly as the heap (no copy — heap and nums are the same list, so this mutates the input)
        heap = nums

        # heapify rearranges the list in place into a min-heap in O(n) — the smallest element is now at heap[0]
        heapq.heapify(heap)

        # Keep going while more than k elements remain — we want to strip the array down to just the k largest
        while len(heap) > k:
            # Pop the smallest element
            heapq.heappop(heap)
            
        # Once exactly k elements remain, they are the k largest. The min-heap top is the smallest of those k → the kth largest
        return heap[0]