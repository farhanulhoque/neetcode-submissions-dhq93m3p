class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Max-Heap + Cooldown Queue (the simulation)

        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1

            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time


        # TC: 
        # SC: 



        # Solution Description: The bottleneck is the most frequent task. If task A appears 5 times and needs a gap of n between each, those 5 As alone force a skeleton of A _ _ ... A _ _ ... A — and we fill the gaps with other tasks (or idle if nothing's available). The greedy strategy: at each cycle, run the most frequent remaining task that isn't cooling down. A max-heap (by remaining count) picks it efficiently. After running a task, it goes into a cooldown queue for n cycles before it can re-enter the heap. If the heap is empty but tasks are still cooling down, the CPU idles.