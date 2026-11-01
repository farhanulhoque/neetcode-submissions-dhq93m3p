class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0":
            return 0
        
        prev2 = 1
        prev1 = 1

        for i in range(1, len(s)):
            curr = 0
            if s[i] != "0":
                curr += prev1
            if "10" <= s[i - 1: i + 1] <= "26":
                curr += prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1


        # TC:
        # SC: 


        # Solution Description: To decode up to position i, the last group was either one digit or two digits: If the single digit s[i-1] is valid (not '0' — can’t be a letter alone), add the ways to decode up to i-1. If the two digits s[i-2:i] form a valid number (10–26), add the ways to decode up to i-2. dp[i] = (s[i-1] valid alone  ? dp[i-1] : 0) + (s[i-2:i] in 10..26  ? dp[i-2] : 0). It’s the Fibonacci recurrence, but each term is gated by a validity check. The tricky part is the zeros: a '0' can never stand alone (no letter maps to 0), so it’s only decodable as part of "10" or "20". We handle base cases and these conditions carefully. Since dp[i] needs only the previous two values, we keep two variables → O(1) space.


        # ----- Deep Dive -----

        # 


        # ----- Edge Cases -----

        # 







