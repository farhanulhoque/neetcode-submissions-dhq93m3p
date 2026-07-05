class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Count frequencies and put them in the hashmap {number: frequency}
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # Maintain a min heap of size k. 
        minHeap = []
        # Loop through each unique number and push (frequence, number) as a tuple so heap sorts by the frequncy (first element)
        for n in count.keys():
            heapq.heappush(minHeap, (count[n], n))
            # If the heap size exceeds k, pop the smallest frequency element out. By keeping the heap at size k and always evicting the smallest, whatever survives in the heap at the end is the top k most frequent elements.
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # Extract Results. 
        result = []
        for i in range(k):
            # Each popped item is (frequency, number) — we grab index [1] for just the number
            result.append(heapq.heappop(minHeap)[1])
        # Return the k most frequent numbers
        return result


        # TC: O(nlogk) -> Each of the n unique numbers gets pushed/popped from a heap of size k. Heap operations cost logk.
        # SC: O(n + k) -> O(n) for count hashmap and O(k) for the heap.

