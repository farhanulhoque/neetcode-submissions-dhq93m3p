class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # This will hold (distance, x, y) tuples
        minHeap = []

        # Iterate over every point
        for x, y in points:
            # calculate distance from origin (no sqrt needed)
            dist = x*x + y*y
            # Store (dist, x, y) — dist first so the heap sorts by it
            minHeap.append((dist, x, y))
        
        # heapify all points into a min-heap in O(n)
        heapq.heapify(minHeap)

        # This is to collect the k closest points
        result = []
        # Pop the k smallest-distance points, extracting their coordinates
        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            result.append([x, y])
        
        # Return the k closest points
        return result


        # TC: O(n + klogn) -> loop: O(n) + heapify: O(n) + heappop: klogn = O(n + klogn). each heappop is O(log n) (the heap has ~n elements) we do it k times → k × O(log n) = O(k log n). they happen one after another (sequential), not nested. build, THEN heapify, THEN pop — so we sum their costs.
        # SC: O(n) -> The heap stores ALL n points as (dist, x, y) tuples → O(n). Even though we only WANT k points, this approach holds all n in the heap at once before popping. So space is O(n) regardless of how small k is.


        # Solution Description: We need the k points with the smallest distance to the origin. A heap ranks points by distance efficiently. Min-heap of all points: put every point in a min-heap keyed by distance, then pop k times to get the k closest. Simple: O(n) to build + O(k log n) to extract. The key optimization for both: compare squared distances, skipping the expensive sqrt — since sqrt is monotonic, it doesn't change the ordering.


        # ----- Deep Dive -----

        # Why the distance goes FIRST in the tuple -> Placing dist first in the tuple makes the heap rank by distance, since Python compares tuples left-to-right. The coordinates trail behind (serving as harmless tiebreakers). This "sort key first in the tuple" idiom is how you control heap ordering.

        # Why we skip the square root -> sqrt is MONOTONIC (increasing): if a² < b², then sqrt(a²) < sqrt(b²). So comparing SQUARED distances gives the SAME ordering as comparing real distances — but skips the expensive sqrt computation. sqrt is a costly floating-point operation. Skipping it (n times) is faster AND avoids float precision issues.

        # Why heapify + pop k, not sort -> Using heapify (O(n)) then popping k times (O(k log n)) is O(n + k log n) — better than a full sort (O(n log n)) when k is small. We only extract the k we need instead of ordering everything. (For k close to n, they're comparable.)







        