class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if (self.small and self.large and -self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
    

    # TC: 
    # SC: 

    # Solution Description: The median splits the sorted data into a smaller half and a larger half. The key insight: we don't need the whole thing sorted — we just need fast access to the boundary between those halves. We maintain two heaps: a max-heap for the smaller half (its top is the largest of the small values — the left boundary), a min-heap for the larger half (its top is the smallest of the large values — the right boundary). We keep the two heaps balanced in size (equal, or the small half has one extra). Then: odd count → the median is the top of the larger heap (the extra element), even count → the median is the average of both heaps' tops. Both addNum and findMedian become efficient: O(log N) to insert, O(1) to read the median.


    # ----- Deep Dive ----- 

    # 