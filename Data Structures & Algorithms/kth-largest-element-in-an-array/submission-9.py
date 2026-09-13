class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min-Heap of Size K

        # this will hold the k largest
        heap = []

        # Push each number into the heap
        for num in nums:
            heapq.heappush(heap, num)

            # If the heap exceeds k, pop the smallest — keep only the k largest
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Heap top = smallest of the k largest = kth largest
        return heap[0]


        # TC: O(nlogk) -> heappush → the heap has AT MOST k elements → a push sifts up at most log k levels → O(log k). heappop (sometimes) → also on a heap of size ≤ k → O(log k). So each iteration costs O(log k). TOTAL = (n iterations) × (O(log k) per iteration) = O(n log k). Capping at k is what makes it O(log k) per operation.
        # SC: O(k) -> The heap holds AT MOST k elements at any time (we pop to keep it ≤ k). When k << n, O(k) is very small — a big advantage.


        # Solution Description: maintain a heap of the k largest; the top (smallest of the k largest) is the kth largest. O(n log k). This is the "expected without sorting" answer and directly reuses the Kth Largest in a Stream pattern.


        # ----- Deep Dive -----

        # Why min-heap of size k gives the kth largest -> keep the k largest values in a min-heap. The smallest of those k (the heap top) is the kth largest.







        