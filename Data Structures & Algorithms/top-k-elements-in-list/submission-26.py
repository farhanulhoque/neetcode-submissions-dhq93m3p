class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, cnt in count.items():
            freq[cnt].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result