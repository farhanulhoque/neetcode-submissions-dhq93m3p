class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-s for s in stones]
        heapq.heapify(heap)


        while len(heap) > 1:
            first = -heapq.heappop(heap)  
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -(first - second))   

        return -heap[0] if heap else 0   


        # TC: O(nlogn) -> heapify is O(n). Then each simulation step does 2 pops + up to 1 push, each O(log n). There are up to O(n) steps (each removes at least one stone), so O(n log n) total
        # SC: O(m) -> The heap holds up to n stones


        # Solution Description: We repeatedly need the two heaviest stones, smash them, and possibly return a leftover stone to the pile. Since the weights keep changing, sorting once isn't enough — we need a structure that gives the max on demand: a max-heap. Each step: pop the two largest (y and x, with y ≥ x). If they differ, push y - x back. Repeat until 0 or 1 stones remain. Python only has a min-heap, so we store negated weights — the "smallest negative" is the "largest positive," giving max-heap behavior.


        # ----- Deep Dive -----

        # Why O(n log n) and not O(n²)? -> Each step removes at least one stone (either both destroyed, or two out and one back = net −1). So there are at most n steps, each O(log n) for the heap operations → O(n log n). Compare with re-sorting every step (O(n² log n)) — the heap's O(log n) per operation is the win

        # 






        