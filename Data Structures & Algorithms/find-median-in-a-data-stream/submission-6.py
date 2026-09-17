class MedianFinder:

    def __init__(self):
        # a max-heap (negated) holding the smaller half. Its top (-small[0]) is the largest small value
        self.small = []
        # a min-heap holding the larger half. Its top (large[0]) is the smallest large value
        self.large = []

    def addNum(self, num: int) -> None:
        # Push the new number into small (negated for the max-heap) — a default landing spot
        heapq.heappush(self.small, -num)

        # If small's top exceeds large's top, the halves are out of order
        if (self.small and self.large and -self.small[0] > self.large[0]):
            # Move the offending value from small to large (un-negate on the way)
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # If small is too big (more than 1 larger than large), move its top to large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # If large is too big, move its top to small (re-negate)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # Odd count, extra in small → median is small's top (un-negated)
        if len(self.small) > len(self.large):
            return -self.small[0]
        # Odd count, extra in large → median is large's top
        if len(self.large) > len(self.small):
            return self.large[0]
        # Even count → average both tops
        return (-self.small[0] + self.large[0]) / 2
    

    # TC: addNum -> O(logn); heappush: O(log N), up to 2 rebalancing moves (pop + push each): O(log N) each, constant number of heap operations, each O(log N)
    #     findMedian -> O(1); just peek one or both heap tops (heap[0] is O(1))
    # SC: addNum -> O(N); the two heaps together hold all N numbers where N = total numbers added so far.
    #     findMedian -> O(1); no new structures

    # Solution Description: The median splits the sorted data into a smaller half and a larger half. The key insight: we don't need the whole thing sorted — we just need fast access to the boundary between those halves. We maintain two heaps: a max-heap for the smaller half (its top is the largest of the small values — the left boundary), a min-heap for the larger half (its top is the smallest of the large values — the right boundary). We keep the two heaps balanced in size (equal, or the small half has one extra). Then: odd count → the median is the top of the larger heap (the extra element), even count → the median is the average of both heaps' tops. Both addNum and findMedian become efficient: O(log N) to insert, O(1) to read the median.


    # ----- Deep Dive ----- 

    # Why two heaps put the median at the boundary ->  The median lives at the boundary between the smaller and larger halves. We don't need everything sorted — just the two boundary values: the largest of the small half (a max-heap's top) and the smallest of the large half (a min-heap's top). Two heaps give O(1) access to exactly those, with O(log N) inserts — beating a sorted list's O(N) inserts.

    # Why small is a max-heap and large is a min-heap -> small = the SMALLER half. We need its LARGEST value (the boundary, closest to the median). A MAX-heap keeps the largest on top. large = the LARGER half. We need its SMALLEST value (the boundary, closest to the median). A MIN-heap keeps the smallest on top. The tops of the two heaps are the two values CLOSEST to the median — they "face each other" across the boundary. 
    
    # Why we must keep the halves ORDERED -> For "boundary = median" to work, EVERY element in small must be <= EVERY element in large. Otherwise the "halves" aren't really the smaller/larger halves. When we push a new number into small, it might be LARGER than large's smallest. When a newly inserted value makes small's top exceed large's top, the halves overlap — so we move that value across to large.

    # For the median to be AT the boundary, the two halves must be equal in size (even total) or differ by exactly 1 (odd total). If one heap grows more than one larger than the other, the true middle drifts away from the tops — so we move the oversized heap's top across to rebalance. This maintains |len(small) − len(large)| ≤ 1.

    # Why findMedian has three cases -> Three cases: odd with extra in small → median is small's top; odd with extra in large → median is large's top; even → average both tops (the two middle values). The even case works because small's top and large's top are exactly the two middle elements in sorted order.







    