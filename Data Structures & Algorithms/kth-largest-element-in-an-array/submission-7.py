class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Heapify-all and shrink

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


        # TC: O(n + (n - k)logn) -> heapify builds a heap from all n elements in O(n). the while loop (pop until size k): we start at size n, pop until size k → we pop (n − k) times. each heappop is O(log n) → (n − k) pops × O(log n) each = O((n − k) log n). TOTAL = O(n) + O((n − k) log n) = O(n + (n − k) log n).
        # SC: O(1) -> heap = nums reuses the input list (heapify is in-place), no new array is allocated. This beats the size-k approach's O(k). The one caveat: it mutates nums (rearranges and shrinks it), so if the caller needs the original array preserved, you'd copy first with list(nums) — which costs O(n) space.


        # ----- Deep Dive -----

        # The tradeoff: This approach pops (n − k) times, so it's fast when k is large (few pops → close to O(n)). The size-k approach pushes/pops on a small heap, so it's fast when k is small (O(n log k) with tiny log k). Neither dominates — they're mirror images. Your version wins for large k; the size-k version wins for small k.

        # 



        

