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


        # TC: O(n) -> the loop processes each character once → O(n) iterations. Each iteration does O(1) work (two validity checks, an add, two assignments). The substring slice s[i-1:i+1] is a fixed 2-char slice → O(1). O(n) overall.
        # SC: O(1) -> only three variables (prev2, prev1, curr) regardless of n. No array, no recursion. O(1) — the space-optimized form.

        # Full-array bottom-up: O(n) space. Naive recursion: O(2ⁿ) time. This optimized version: O(n) time, O(1) space.


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
        


        # Why the two-digit check is "10" <= ... <= "26" -> A two-digit group is a valid letter only if it's in the range 10–26 (J–Z... wait, 10=J, 26=Z). So we check the two-char substring s[i-1:i+1] is between "10" and "26". 

                # Why 10 as the LOWER bound (not 01)?
                #     "01" through "09" have a LEADING ZERO → invalid (the problem says leading
                #     zeros aren't allowed). A valid two-digit code starts at 10. So the lower
                #     bound is 10, which also naturally excludes "00"–"09".

                # Why 26 as the UPPER bound?
                #     Z = 26 is the highest letter. "27"–"99" don't map to any letter → invalid.

                # The string comparison "10" <= pair <= "26" works because two-char numeric strings
                # compare lexicographically the same as numerically (same length, digit by digit).
                #     (alternatively: 10 <= int(s[i-1:i+1]) <= 26 — same check, numeric.)

                # The range [10, 26] precisely captures all valid two-digit letter codes, excluding
                # leading-zero codes (below 10) and out-of-range codes (above 26).

        

        # Why base cases are both 1 (including the “empty = 1 way”) -> 

                # prev1 = 1 (ways to decode s[0]): if the first char is valid (not '0', ensured by
                #     Line 1's check), there's exactly 1 way to decode a single valid digit.

                # prev2 = 1 (ways to decode the EMPTY prefix): this is the subtle one. It represents
                #     "one way to decode nothing" — the empty string.

                # Why does empty = 1 matter? When a two-digit group at the START is valid (e.g.
                # "12"), decoding it uses dp[i-2] = dp[empty] = prev2 = 1. If prev2 were 0, we'd
                # undercount — "12" → "L" (via the 2-digit group) wouldn't be counted.

                #     "12": i=1. 2-digit "12" in 10..26 → curr += prev2 = 1 → counts the "L"
                #     decoding. The empty-prefix base case of 1 is what makes this work.

                # This "empty = 1 way" base case is a common DP convention: there's exactly one way
                # to do nothing, and it anchors recurrences that reach back to the start.



        # ----- Edge Cases -----

        # Leading zero ("0...") -> Line 1 returns 0 — a string starting with '0' can’t be decoded.

        # Single valid digit ("5") -> Loop doesn’t run; returns prev1 = 1.

        # Standalone zero ("30") -> '0' can’t stand alone (1-digit skipped) and "30" not in 10–26 (2-digit skipped) → curr = 0 → returns 0.

        

        # Visual Walkthrough:

            # s = "1012"

            # ── Line 1: s[0]='1' != '0' → proceed ──
            #     prev2 = 1 (empty prefix), prev1 = 1 (first char '1')

            # ── i=1 (s[1]='0') ──
            #     curr = 0
            #     1-digit: s[1]='0' → '0', condition fails → skip (can't stand alone)
            #     2-digit: s[0:2]="10", "10" <= "10" <= "26"? YES → curr += prev2 = 1 → curr=1
            #     (the "10" → J decoding)
            #     slide: prev2=1, prev1=1

            # ── i=2 (s[2]='1') ──
            #     curr = 0
            #     1-digit: s[2]='1' != '0' → curr += prev1 = 1 → curr=1
            #     2-digit: s[1:3]="01", "10" <= "01"? NO (leading zero) → skip
            #     (so far "101" → "JA", via the single '1')
            #     slide: prev2=1, prev1=1

            # ── i=3 (s[3]='2') ──
            #     curr = 0
            #     1-digit: s[3]='2' != '0' → curr += prev1 = 1 → curr=1
            #     2-digit: s[2:4]="12", "10" <= "12" <= "26"? YES → curr += prev2 = 1 → curr=2
            #     (two decodings: "JAB" via single '2', and "JL" via "12")
            #     slide: prev2=1, prev1=2

            # ── Result ──
            #     return prev1 = 2 

            # The 2 decodings of "1012": "JAB" (10|1|2) and "JL" (10|12). Note "1|01|2" was
            # correctly EXCLUDED — "01" has a leading zero (caught at i=2's 2-digit check).
            # Each position summed its valid 1-digit and 2-digit options.







