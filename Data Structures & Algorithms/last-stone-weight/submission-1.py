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


        # Solution Description: We repeatedly need the two heaviest stones, smash them, and possibly return a leftover stone to the pile. Since the weights keep changing, sorting once isn't enough — we need a structure that gives the max on demand: a max-heap. Each step: pop the two largest (y and x, with y ≥ x). If they differ, push y - x back. Repeat until 0 or 1 stones remain. Python only has a min-heap, so we store negated weights — the "smallest negative" is the "largest positive," giving max-heap behavior.