class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quickselect (Avg O(n) but worst case O(n^2))

        # Convert: the kth largest is at index len(nums) - k in ascending sorted order
        k = len(nums) - k
        # Helper operating on the range [left, right]
        def quickselect(left, right):
            # Choose the rightmost element as the pivot
            pivot = nums[right]

            # This is the boundary where elements ≤ pivot will be on the left and elements >= pivot will be on the right
            p = left
            # Partition: move every element ≤ pivot to the left region, advancing p
            for i in range(left, right):
                if nums[i] <= pivot: 
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            # Place the pivot at its final sorted position p (swap it into place)
            nums[p], nums[right] = nums[right], nums[p]

            # The kth element is to the right → recurse right
            if p < k:
                return quickselect(p + 1, right)
            # The kth element is to the left → recurse left
            elif p > k:
                return quickselect(left, p - 1)
            # p == k → the pivot IS the kth element → return it
            else:
                return nums[p]
        
        # Start on the full array
        return quickselect(0, len(nums) - 1)
            

        # TC: O(n) average, O(n²) worst case -> After partitioning, we recurse into only ONE side (the side with our target k), discarding the other. On average, a random-ish pivot splits the range roughly in half. TOTAL work = n + n/2 + n/4 + n/8 + ... -> n + n/2 + n/4 + ... = n × (1 + 1/2 + 1/4 + ...) = n × 2 = 2n → O(2n) = O(n) average. 
        # SC: O(1) -> The algorithm is in-place (only swaps within nums), so the data uses O(1) extra space. The recursion call stack adds O(log n) on average (halving depth) or O(n) worst case — writing it iteratively removes even that, giving O(1) always.
        
        # The worst case happens when the pivot is always the SMALLEST or LARGEST element in the range — so partitioning only peels off ONE element each time. Then the range sizes shrink by just 1 each step: n + (n-1) + (n-2) + ... + 1 -> This is the arithmetic series that sums to n(n+1)/2: ≈ n²/2 → O(n²). When does this happen? A FIXED pivot (like always nums[right]) on already-sorted input: every pivot is the max → peel off one element at a time → O(n²). A random pivot makes that astronomically unlikely, preserving O(n) expected.


        # Solution Description: Pick a pivot, partition the array so smaller elements go one side and larger the other. After partitioning, the pivot is in its final sorted position. If that position is the one we want (the kth largest), we're done; otherwise recurse into just one side. Because we only recurse into one half each time, it's O(n) on average.


        # -----  Deep Dive -----

        # The core idea — partition isolates one position -> PARTITION: pick a pivot, rearrange so: [ elements <= pivot ] [ pivot ] [ elements > pivot ]. After partitioning, the pivot is in its FINAL SORTED POSITION. everything left of it is smaller, everything right is larger. So we KNOW the pivot's rank without sorting the rest! The Quickselect leap over quicksort: Quicksort recurses into BOTH sides (to fully sort) → O(n log n), Quickselect recurses into ONLY ONE side → O(n) average. We only care about ONE position (the kth). After partitioning: if pivot is at our target index → done, if target is left of pivot  → recurse left only, if target is right of pivot → recurse right only. Discarding half the array each time → O(n) average (n + n/2 + n/4 + ... = 2n).

        # Why k = len(nums) - k (the index conversion) -> Quickselect's partition arranges elements in ascending order (smaller elements to the left, larger to the right). So it naturally works with positions counted from the left — i.e., the kth smallest. But the problem asks for the kth largest. So we need to translate "kth largest" into "which position from the left." The kth largest sits at index n - k in an ascending-sorted array. In an ascending array of n elements: the LARGEST is at the LAST index (n-1), the kth largest is k positions from the end. "k positions from the end" = index (n - k). 

        # When p and i are the same index, the swap does nothing visible — but p still advances. This just means "this element is already in the right region, extend the boundary." Early elements that are ≤ pivot often produce these harmless self-swaps. p marks the end of the "≤ pivot" region, and i scans ahead; whenever i finds a small element, it's swapped back to p (growing the region), and big elements that i passes over get pushed right when a later small element swaps with them. At the end, p is the gap between small and big — exactly where the pivot drops in.

        # The line "nums[p], nums[right] = nums[right], nums[p]" -> we chose the pivot as nums[right] (the rightmost element), and the partition loop never touches it — the loop runs range(left, right), which stops before right. So during the whole loop, the pivot just SITS at index `right`, waiting. After the loop, p is now pointing at the first element that is greater than the pivot — which is exactly where the pivot should go. The swap line moves the pivot from its temporary parking spot (index right) to its correct sorted position (index p). The swap also moves the element that was at p (a "> pivot" element) over to index right. That's fine — it's a larger-than-pivot element, and right is now part of the "> pivot" region, so it lands where it belongs.

        # How the partition loop works (Lomuto scheme) -> This is the Lomuto partition. `p` marks the boundary: everything before p is <= pivot. We scan with i; whenever we find an element <= pivot, we swap it into the "<= region" and grow that region (p += 1). p = "next slot for a <=pivot element", i = "scanner walking through the array". At the end, p is where the pivot belongs. We swap the pivot (at `right`) into position p → pivot is now in its final sorted spot.

        # Why recurse into only ONE side -> We recurse into exactly ONE side — the one containing index k. The other side is discarded entirely (we don't care about it). This is why it's O(n) average, not O(n log n): each step throws away roughly half, and we never revisit the discarded half. 
        
        # Why random pivot avoids O(n²) -> Quickselect's WORST case is O(n²): if the pivot is always the smallest or largest, each partition only shrinks the range by 1 → n + (n-1) + ... = O(n²). This happens on already-sorted input with a fixed (rightmost) pivot. Fix: pick a RANDOM pivot. Then the worst case becomes astronomically unlikely — expected O(n) regardless of input order. swap a random element to the `right` position before partitioning → the pivot is now random → average O(n) holds even on sorted input.








        