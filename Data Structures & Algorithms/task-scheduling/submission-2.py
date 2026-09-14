class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Math Formula (the O(N) shortcut)

        counts = Counter(tasks)                          
        maxCount = max(counts.values())                  
        numMax = sum(1 for c in counts.values() if c == maxCount)  

        # skeleton length vs. total tasks — take the larger
        return max(len(tasks), (maxCount - 1) * (n + 1) + numMax)