class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        minHeap = []
        for n in count.keys():
            heapq.heappush(minHeap, (count[n], n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        result = []
        for i in range(len(minHeap)):
            result.append(heapq.heappop(minHeap)[1])
        
        return result