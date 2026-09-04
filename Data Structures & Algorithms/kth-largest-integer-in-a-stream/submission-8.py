class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Store k for later use in add
        self.k = k
        # Use the input list as our heap storage
        self.minHeap = nums
        # heapify — rearrange the list into a valid min-heap in O(n)
        heapq.heapify(self.minHeap)

        # Shrink the heap down to size k by popping the smallest values (we only keep the k largest)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Push the new value onto the heap (O(log k))
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
    

    # TC: Constructor -> O(n) heapify + O((n-k) log n) shrinking = O(n log n) worst case; add -> O(log k) — one push + at most one pop on a size-k heap
    # SC: O(k) -> the heap holds at most k values
    

    # Solution Description: Maintain a min-heap containing only the k largest values seen so far. If the heap always holds exactly the k largest values, then the smallest of those k values — which sits at the top of a min-heap — is the kth largest overall. When a new value arrives, push it onto the heap. If the heap now exceeds size k, pop the smallest (it can't be among the k largest). The heap top is always the answer. This gives O(log k) per add — far better than re-sorting (O(n log n)) every time.


    # ----- Deep Dive -----

    # 







