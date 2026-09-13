class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min-heap of size k

        heap = nums

        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return heap[0]