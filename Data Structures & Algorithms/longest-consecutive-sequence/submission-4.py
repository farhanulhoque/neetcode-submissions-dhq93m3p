class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Convert nums array to a set - enables O(1) lookups and removes duplicates
        numSet =  set(nums)
        # This is to track the longest sequence found so far
        longest = 0

        # Iterate through the set
        for n in numSet:
            # Only start counting if n is the start of a sequence — i.e. n - 1 doesn't exist
            if (n - 1) not in numSet:
                # This number is a sequence start - initialize length to 1
                length = 1
                # Keep extending the sequence as long as the next number exists in the set. Increment length for each consecutive number found
                while (n + length) in numSet:
                    length += 1
                # Update longest if this sequence is the best so far
                longest = max(longest, length) 
        
        return longest

        # TC: O(n) -> Building the set is O(n) + Each number visited at most twice (outer + while loop): O(n)
        # SC: O(n) -> set stores all  n numbers

        # Why not O(n^2) -> The while loop only runs for sequence starts. Every number is visited by the while loop at most once across the entire execution. Its total iterations across the entire run is at most n — same golden rule as bucket sort!
    
