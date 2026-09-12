class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min-heap of size k

        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]