class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        # Build the empty buckets. Create n + 1 empty buckets because frequencies go from 1 to n inclusive. The index represents the frequency. There is an extra bucket at index 0 beacause we want frequency to map directly to an index (starting with 1). Starting at index 1 naturally keeps the mapping clean, and index 0 just sits there unused.
        freq = [[] for i in range(len(nums) + 1)]

        # Build {number: frequency} hashmap.
        for n in nums:
            count[n] = count.get(n, 0) + 1
        # Loop throgh each (frequency, number) pair and drop the number into the bucket matching its frequency.
        for n, cnt in count.items():
            freq[cnt].append(n)
        
        result = []
        # Read from the last bucket (highest frequency) and go down to index 1
        for i in range(len(freq) - 1, 0, -1):
            # Loop through all numbers in this frequency bucket and add to result
            for n in freq[i]:
                result.append(n)
                # Stop exactly when we have k elements.
                if len(result) == k:
                    return result
        

        # TC: O(n) -> Counting pass O(n) + Bucket fill O(n) + Bucket Scan O(n) - all linear. 
        # SC: O(n) -> count hashmap + freq array both scale with n.

        # Why is TC not O(n^2) ->  nested loop is only O(n²) if the inner loop runs n times for each outer loop iteration. Here, the inner loop doesn't run n times per outer iteration, it runs however many numbers are in that bucket. No matter how the numbers are distributed across buckets, the total across all buckets is always exactly n — because every number lands in exactly one bucket.
        # When a nested loop's total iterations across all inner runs equals n, the overall complexity is O(n)

