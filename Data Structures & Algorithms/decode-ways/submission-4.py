class Solution:
    def numDecodings(self, s: str) -> int:
        
        # If the string starts with '0', it can’t be decoded at all (no letter maps to a leading 0) → return 0
        if s[0] == "0":
            return 0
        
        # prev2 = ways to decode the empty prefix = 1 (one way: decode nothing)
        prev2 = 1
        # prev1 = ways to decode the first character = 1 (valid since we passed Line 1)
        prev1 = 1

        # Process each character from index 1 onward
        for i in range(1, len(s)):
            # curr = ways to decode up to position i, start at 0
            curr = 0
            # If the single digit s[i] isn’t '0' (valid as a standalone letter), 
            if s[i] != "0":
                # add the ways to decode up to the previous char (prev1)
                curr += prev1
            # If the two digits s[i-1:i+1] form a number in 10–26 (a valid two-letter grouping)
            if "10" <= s[i - 1: i + 1] <= "26":
                # add the ways to decode up to two chars back (prev2)
                curr += prev2
            # Slide the window: prev2 becomes the old prev1
            prev2 = prev1
            # prev1 becomes the new curr
            prev1 = curr
        
        # Return the total ways to decode the whole string
        return prev1


        # TC:
        # SC: 


        # Solution Description: To decode up to position i, the last group was either one digit or two digits: If the single digit s[i-1] is valid (not '0' — can’t be a letter alone), add the ways to decode up to i-1. If the two digits s[i-2:i] form a valid number (10–26), add the ways to decode up to i-2. dp[i] = (s[i-1] valid alone  ? dp[i-1] : 0) + (s[i-2:i] in 10..26  ? dp[i-2] : 0). It’s the Fibonacci recurrence, but each term is gated by a validity check. The tricky part is the zeros: a '0' can never stand alone (no letter maps to 0), so it’s only decodable as part of "10" or "20". We handle base cases and these conditions carefully. Since dp[i] needs only the previous two values, we keep two variables → O(1) space.


        # ----- Deep Dive -----

        # The validity-gated recurrence (counting, but conditional) -> A Fibonacci-like sum where each term is conditional. Like Climbing Stairs, the ways to reach position i = ways via a 1-step + ways via a 2-step. But here each "step" must be a VALID decoding:

                # 1-DIGIT step: decode s[i] as a single letter. Valid only if s[i] != '0'
                #               (no letter maps to 0). If valid, add dp[i-1] (ways up to the prev char).

                # 2-DIGIT step: decode s[i-1:i+1] as a two-digit letter. Valid only if it's in
                #               10..26 (the valid two-digit letter codes). If valid, add dp[i-2].

                # dp[i] = (1-digit valid ? dp[i-1] : 0) + (2-digit valid ? dp[i-2] : 0).

                # Unlike plain Climbing Stairs (both terms always added), here each term is GATED: only add it if that grouping is a legal letter. curr starts at 0 and accumulates only the valid options.
        


        # Why zeros are the central difficulty -> The mapping is A=1 ... Z=26. There's NO letter for 0. So a '0' can NEVER be decoded as a standalone digit — it MUST be part of "10" or "20". 

                # Consequences:
                #     - a single '0' (not preceded by 1 or 2) is UNDECODABLE → 0 ways.
                #         e.g. "30": '3' alone is fine, but '0' can't stand alone AND "30" isn't
                #         in 10..26 → NO valid decoding → 0 ways.
                #     - '0' only works inside "10" (→ J) or "20" (→ T).
                
                # So the 1-digit transition is SKIPPED when s[i] == '0' (condition fails
                #     → curr doesn't get prev1). The ONLY way a '0' contributes is via the 2-digit
                #     transition, IF the pair is "10" or "20".
                
                # "10": s[1]='0' → 1-digit skipped. "10" in 10..26 → 2-digit adds prev2 → 1 way.
                # "20": similar → 1 way. "30","40",...,"90","00": neither transition valid → 0 ways.
        

        
                                    


        # ----- Edge Cases -----

        # 







