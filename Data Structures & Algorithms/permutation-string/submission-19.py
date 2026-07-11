class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 longer than s2 → no window fits → early exit
        if len(s1) > len(s2):
            return False

        # Two count arrays of 26 — one for s1, one for the current window
        s1Count, s2Count = [0] * 26, [0] * 26
        # Build the initial window over the first len(s1) characters
        for i in range(len(s1)):
            # Count characters in s1
            s1Count[ord(s1[i]) - ord('a')] += 1
            # Count characters in s2's first window
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # If initial window already matches → Return true
        if s1Count == s2Count:
            return True

        # Initialize the left pointer
        left = 0
        # right pointer starts at len(s1) — first character past the initial window. The window [0 ... len(s1)-1] already exists before the sliding loop starts as the first window was already built in the setup loop. If right started at 0, we'd be re-adding characters already counted — double counting.
        for right in range(len(s1), len(s2)):
            # Character entering on the right — increment its count
            s2Count[ord(s2[right]) - ord('a')] += 1
            # Character leaving on the left — decrement its count
            s2Count[ord(s2[left]) - ord('a')] -= 1

            # Slide the left pointer forward
            left += 1

            # Compare all 26 buckets — if identical, it's a permutation
            if s1Count ==  s2Count:
                return True
        # Return false if the loop ended with no match
        return False


        # TC: O(n) -> n slides, each doing a 26-element comparison. 26 is a constant, so it reduces to O(n)
        # SC: O(1) -> Two fixed arrays of 26 characters

        # Solution Description: A permutation of s1 is an anagram — same character counts, any order. Build a 26-slot frequency array for s1, then slide a fixed-size window of length len(s1) across s2, keeping a matching count array for the window. Each slide increments the entering character and decrements the leaving one. After each slide, compare the two arrays — if all 26 counts match, it's a permutation. Arrays compare position by position, so leftover zeros are harmless.
        
        # The 26n is worth stating explicitly in an interview even though it simplifies to O(n). It shows you know exactly where the work is — and it's the perfect setup for offering the matches optimization: "I can drop this 26-factor to O(1) per slide by tracking how many buckets match."
        # The optimal version replaced this with a single matches == 26 check by tracking match changes incrementally. Here, we just brute-force compare all 26 each time — simpler to write, slightly more work per step.
