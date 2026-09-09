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
        
        # If the heap now exceeds k, pop the smallest — it's not among the k largest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The heap top (heap[0]) is the smallest of the k largest = the kth largest
        return self.minHeap[0]
    

    # TC: Constructor -> O(n) heapify + O((n-k) log n) shrinking = O(n log n) worst case; add -> O(log k) — one push + at most one pop on a size-k heap
    # SC: O(k) -> the heap holds at most k values
    

    # Solution Description: Maintain a min-heap containing only the k largest values seen so far. If the heap always holds exactly the k largest values, then the smallest of those k values — which sits at the top of a min-heap — is the kth largest overall. When a new value arrives, push it onto the heap. If the heap now exceeds size k, pop the smallest (it can't be among the k largest). The heap top is always the answer. This gives O(log k) per add — far better than re-sorting (O(n log n)) every time.


    # ----- Deep Dive -----

    # Why a MIN-heap for the kth LARGEST -> We keep ONLY the k largest values in a heap. Then among those k values, the SMALLEST one is exactly the kth largest overall. If you have the top k values, ranked: 1st largest, 2nd largest, ..., kth largest - The kth largest is the SMALLEST of this group. A MIN-heap keeps its smallest element at the top (heap[0]). So heap[0] = the smallest of the k largest = the kth largest. This is why you use a min-heap for a largest query. 

    # Why we cap the heap at size k -> We only care about the k LARGEST values. Anything smaller than the current k largest is irrelevant — it can never be the kth largest (too small). So whenever the heap grows beyond k, we pop the smallest (the min-heap top). That discarded value was the smallest in the heap → not among the k largest → safe to drop. heap has k+1 values → the smallest can't be in the "top k" → pop it → heap back to size k, still holding the k largest. This keeps the heap SMALL (size k), which is why operations are O(log k), not O(log n). If n is huge but k is small, this is a massive win.

    # Why heapify is O(n), not O(n log n) -> heapify builds a heap from a list in O(n), not O(n log n), using a bottom-up sift-down process (rearrange in place). This is faster than pushing elements one at a time. It's a good fact to know — building a heap from existing data should always use heapify, not repeated heappush. 

    # Why the initial shrink loop uses while, not if -> The initial nums could have MANY more than k values. E.g. k=2 but nums has 100 values → we must pop 98 times to get down to size k. So we use a WHILE loop (pop repeatedly until size == k). Contrast with add(), which uses an IF: add() pushes exactly ONE value, so the heap grows by at most 1 over k → a single pop suffices → if, not while. The distinction: bulk-shrink vs incremental-maintain.







