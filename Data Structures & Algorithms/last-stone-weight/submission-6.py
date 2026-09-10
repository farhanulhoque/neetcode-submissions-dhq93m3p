class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Negate every weight — so the min-heap behaves like a max-heap
        heap = [-s for s in stones]
        # heapify into a valid heap in O(n)
        heapq.heapify(heap)

        # Keep smashing while at least 2 stones remain
        while len(heap) > 1:
            # Pop the largest (negate back to positive)
            first = -heapq.heappop(heap)
            # Pop the next largest  
            second = -heapq.heappop(heap)

            # If they differ, the leftover y - x goes back (negated) into the heap
            if first != second:
                heapq.heappush(heap, -(first - second))   

        # Return the last stone (negated back), or 0 if the heap is empty
        return -heap[0] if heap else 0   


        # TC: O(nlogn) -> heapify is O(n). Then each simulation step does 2 pops + up to 1 push, each O(log n). There are up to O(n) steps (each removes at least one stone), so O(n log n) total
        # SC: O(n) -> The heap holds up to n stones


        # Solution Description: We repeatedly need the two heaviest stones, smash them, and possibly return a leftover stone to the pile. Since the weights keep changing, sorting once isn't enough — we need a structure that gives the max on demand: a max-heap. Each step: pop the two largest (y and x, with y ≥ x). If they differ, push y - x back. Repeat until 0 or 1 stones remain. Python only has a min-heap, so we store negated weights — the "smallest negative" is the "largest positive," giving max-heap behavior.


        # ----- Deep Dive -----

        # Why O(n log n) and not O(n²)? -> Each step removes at least one stone (either both destroyed, or two out and one back = net −1). So there are at most n steps, each O(log n) for the heap operations → O(n log n). Compare with re-sorting every step (O(n² log n)) — the heap's O(log n) per operation is the win

        # The negation trick — simulating a max-heap with a min-heap -> Python's heapq is ONLY a min-heap (pops the smallest). But we want the LARGEST. Trick: store negated values. Then: the SMALLEST negative = the LARGEST original. Two negations to remember: PUSH: negate going in -> heappush(heap, -value), POP:  negate coming out -> value = -heappop(heap). The negatives live only inside the heap; you flip back whenever you read. Negate on the way in (-value), negate on the way out (-heappop(...)). 

        # Why y ≥ x automatically (pop order) -> Because a max-heap pops the largest first, y (first pop) is always ≥ x (second pop) — no comparison needed. This guarantees y - x ≥ 0, matching the problem's setup where the heavier stone survives.

        # Why we only push back when y != x -> We push back only when y != x — if they're equal, both stones are destroyed and nothing remains to add. Skipping the y == x case avoids inserting a useless 0-weight stone. (Pushing 0 would technically work but adds meaningless entries.)

        # Why the final check handles the empty case -> The loop ends when len(heap) <= 1. Two possible end states: heap has 1 stone → return it (negated back): -heap[0],  heap is EMPTY → all stones destroyed → return 0. The "if heap else 0" guards against reading heap[0] on an empty heap (which would crash with IndexError).







        