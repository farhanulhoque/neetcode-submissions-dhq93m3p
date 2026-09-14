class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Max-Heap + Cooldown Queue (the simulation)
        
        # Count how many times each task appears (frequency map)
        count = Counter(tasks)
        # Build a max-heap of counts (negated, since Python's heap is a min-heap)
        heap = [-cnt for cnt in count.values()]
        # heapify in O(k)
        heapq.heapify(heap)

        # time = the running cycle count (our answer)
        time = 0
        # Cooldown queue holding (remainingCount, readyTime) for tasks on cooldown
        q = deque()

        # Keep going while there are tasks in the heap or cooling down
        while heap or q:
            # Each iteration is one CPU cycle → advance time
            time += 1

            # If a task is available
            if heap:
                # pop the most frequent one. +1 on the negative count means "used one instance" (shrinks the remaining count)
                cnt = heapq.heappop(heap) + 1
                # If that task still has instances left (not 0), queue it to become ready at time + n
                if cnt:
                    q.append((cnt, time + n))
            
            # If a cooling-down task is ready now (its readyTime == time), push it back into the heap
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        # When both heap and queue are empty, all tasks are done → time is the answer
        return time


        # TC: 
        # SC: 



        # Solution Description: The bottleneck is the most frequent task. If task A appears 5 times and needs a gap of n between each, those 5 As alone force a skeleton of A _ _ ... A _ _ ... A — and we fill the gaps with other tasks (or idle if nothing's available). The greedy strategy: at each cycle, run the most frequent remaining task that isn't cooling down. A max-heap (by remaining count) picks it efficiently. After running a task, it goes into a cooldown queue for n cycles before it can re-enter the heap. If the heap is empty but tasks are still cooling down, the CPU idles.


        # ----- Deep Dive -----

        # Why "most frequent first" is the right greedy choice -> The most frequent task is the BOTTLENECK. It needs the most cooldown gaps, so it constrains the schedule the most. If you DON'T prioritize it, you waste cycles: the frequent task keeps hitting its cooldown, forcing idles later because you didn't "spread it out" early. Running it greedily (whenever it's available) spreads its unavoidable cooldowns out early, letting other tasks fill the gaps. Delaying it only forces idle cycles later.

        # The cooldown queue — why (count, time + n) -> After running a task at `time`, it can't run again until n cycles have passed. So it becomes available at time + n. We store (remainingCount, readyTime = time + n) in a queue. Each cycle, we check if the FRONT of the queue is ready (readyTime == time). If so, it re-enters the heap (available to run again). Why a QUEUE (FIFO)? -- Because tasks cool down in the ORDER they were used. The one used earliest becomes ready earliest → front of the queue is always the next to become ready. FIFO ordering matches cooldown ordering perfectly.

        # Why cnt = heappop(heap) + 1 (the negation arithmetic) -> Counts are stored NEGATED (for the max-heap). Running the task once should DECREASE the remaining count by 1: real count 3 → 2. In negated form: -3 → -2. To go from -3 to -2, you ADD 1. heappop returns -3 (the most frequent, since -3 is smallest = most negative) -3 + 1 = -2  → represents remaining count 2. So "+1" on a negative number is really "subtract 1 from the real count." If the count is 0, the task is fully scheduled and isn't re-queued.









