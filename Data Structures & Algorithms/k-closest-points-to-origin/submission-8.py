class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max Heap (better when k is much smaller than n)

        heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[x, y] for (_, x, y) in heap]


        # TC: O(n log k) -> each of n points does an O(log k) push/pop. heappush → O(log k)   ← heap has at most k elements, so log k not log n!, maybe heappop → O(log k). TOTAL = n × O(log k) = O(n log k).
        # SC: The heap NEVER exceeds size k (we pop whenever it would) → space is O(k), not O(n). It holds at most k points at any moment. This is the decisive advantage when k ≪ n: dramatically less memory than storing all n points.
        


        # Keep a MAX-heap of size k (negate dist so the FARTHEST is on top).

        # For each point:
        #     push it. If the heap exceeds k, pop the farthest.
        #     → the heap always holds the k CLOSEST seen so far.

        # Why max-heap here? To find the k CLOSEST, we cap at k and evict the
        # FARTHEST when overflowing — that requires quick access to the max (farthest).
        #     → same "min-heap for largest / max-heap for smallest" inversion from before!

        

        