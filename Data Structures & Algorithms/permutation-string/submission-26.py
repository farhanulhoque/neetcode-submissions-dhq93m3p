class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, no window can fit — early exit
        if len(s1) > len(s2):
            return False
        
        # Two count arrays: one for s1, one for the current window in s2
        s1Count, s2Count = [0] * 26, [0] * 26
        # Loop over the first len(s1) characters — this builds the initial window
        for i in range(len(s1)):
            # Count characters in s1
            s1Count[ord(s1[i]) - ord('a')] += 1
            # Count characters in s2's first window — same loop, both at index i
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # Initialize matches. This is the counter for how many of the 26 letters have equal counts
        matches = 0
        # Check all 26 buckets once (only done here, at setup)
        for i in range(26):
            # Increment matches for every bucket where counts agree
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        # Initialize left pointer
        left = 0
        # right pointer starts at len(s1) — the first character past the initial window. The first window was already built in the setup loop so the window [0 ... len(s1)-1] already exists before the sliding loop starts.
        for right in range(len(s1), len(s2)):
            # If all 26 buckets match → the current window is a permutation
            if matches == 26:
                return True
            
            # This is the index of the character entering the window
            i = ord(s2[right]) - ord('a')
            # Increment its count — window now has one more of it
            s2Count[i] += 1
            # If adding it made the counts equal → gained a match
            if s1Count[i] == s2Count[i]:
                matches += 1
            # If adding it made s2Count exceed s1Count by exactly 1 → they were equal, now aren't → lost a match
            elif s1Count[i] + 1 == s2Count[i]:
                matches -= 1

            # This is the index of the character leaving the window
            i = ord(s2[left]) - ord('a')
            # Decrement its count — window now has one fewer
            s2Count[i] -= 1
            # If removing it made the counts equal → gained a match
            if s1Count[i] == s2Count[i]:
                matches += 1
            # If removing it made s2Count fall short by exactly 1 → they were equal, now aren't → lost a match
            elif s1Count[i] - 1 == s2Count[i]:
                matches -= 1
            # Slide the left pointer forward
            left += 1

        # Loop ended — check the final window (never checked inside the loop)
        return matches == 26


        # TC: O(n) -> n = len(s2). The setup loop is O(len(s1)), the 26-bucket init is O(1), and the sliding loop runs n - len(s1) times doing O(1) work per step
        # SC: O(1) -> Two arrays of exactly 26 characters — fixed regardless of input size
        
        # Solution Description:A permutation of s1 is just an anagram of s1 — same character counts, any order. So we slide a window of exactly len(s1) across s2 and check whether the window's character counts match s1's. The naive check compares all 26 counts each step. The optimization: maintain a matches counter tracking how many of the 26 letters currently have equal counts. When a character enters or leaves the window, only that one letter's bucket changes — so we adjust matches by ±1 instead of rescanning all 26. When matches == 26, we've found a permutation.

        # The elif s1Count[i] + 1 == s2Count[i] is checking: "did I just step past equality?" — meaning the counts were equal before this increment.
        # A fixed-size window slides by doing two things per step: Every slide, one character enters on the right, one character leaves on the left. Size stays constant. Those two count updates keep s2Count an accurate mirror of the window — exactly the same principle we discussed with the set and the frequency map earlier.
        # only ONE bucket changes when a character enters, and only ONE bucket changes when a character leaves. So instead of rechecking all 26, we check just the one that moved — and nudge matches by ±1. When matches == 26, all buckets agree → the window is a permutation.