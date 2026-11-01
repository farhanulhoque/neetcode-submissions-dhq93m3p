class Solution:
    def countSubstrings(self, s: str) -> int:
        # Expand Around Center
        
        # Total count of palindromic substrings
        count = 0

        # Helper that expands from a center (left, right) and returns how many palindromes it finds
        def expand(left, right):
            # Count of palindromes found from this center
            cnt = 0
            # Expand while in bounds and the two characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Each successful match is one more palindrome → increment
                cnt += 1
                # Expand the left and right pointers outward
                left -= 1
                right += 1
            # Return the number of palindromes centered here
            return cnt

        # Try every index i as a center
        for i in range(len(s)):
            # Odd center: expand from a single char (l = r = i)
            count += expand(i, i)
            # Even center: expand from between two chars (l = i, r = i+1)
            count += expand(i, i + 1)
        
        # Return the total count
        return count


        # TC: O(n²) -> we try O(n) centers (n odd + n-1 even = 2n-1 = O(n)). Each center expands up to O(n) times (e.g. "aaaa" expands fully). O(n) centers × O(n) expansion each = O(n²). O(n²) overall.
        # SC: O(1) -> only a counter and a few pointers (count, cnt, l, r). No DP table, no extra structures. O(1) extra space.


        # Solutiin Dexcription: Every palindromic substring has a center, so — exactly as in Longest Palindromic Substring — we try every center and expand outward while the characters match. The only change: instead of tracking the longest, we count each valid palindrome. The key realization: every time an expansion step succeeds (s[l] == s[r] within bounds), that’s one more palindromic substring. A center that expands 3 times yields 3 palindromes (the center itself, then one wider, then wider still). We handle both odd centers (single char) and even centers (between two chars), summing the count across all 2n-1 centers.


        # ----- Deep Dive -----

        # Why each expansion step counts one palindrome -> In Longest Palindromic Substring, we tracked the WIDEST expansion. Here we COUNT every expansion. Each time the while loop body runs (s[l] == s[r] within bounds), the current span s[l..r] is a VALID palindrome → count it (cnt += 1). So instead of "keep the longest," we "add up all of them." Same expansion mechanism, different accounting: max → sum. Why this counts correctly: expanding from a center produces a NESTED sequence of palindromes (each one char wider on both sides). Every one in that sequence is a distinct palindromic substring → count each → cnt per center.


        # Why both odd and even centers -> Same two-flavor subtlety from Longest Palindromic Substring:

                # ODD-length palindromes ("aba"): single-char center → expand(i, i).
                # EVEN-length palindromes ("bb"): center between two chars → expand(i, i+1).

                # We must count BOTH. Odd-only would miss all even-length palindromes: "bb": no single char is its center → only the even center (between the two b's) catches it → we'd undercount without expand(i, i+1).

                # For each index i, we run both expansions and add both counts. This covers all 2n-1 centers (n single-char + n-1 between-char), counting every palindrome exactly once. 

                # each palindrome has exactly ONE center, so counting per center = counting each palindrome once (no double-counting).



        # Why single characters are always counted -> Single characters are always counted — the odd expansion expand(i, i) starts with l = r = i, and s[i] == s[i] is trivially true, so it counts at least 1. Each of the n characters contributes one palindrome, so the total is at least n. The even expansion may count 0 (if adjacent chars differ), but the odd center always yields the single char. This guarantees every single-letter palindrome is included.



        # Why the helper returns a count -> The expand(l, r) helper returns a count, keeping the main loop clean — for each center, we just add the two expansion counts (expand(i, i) + expand(i, i+1)). This encapsulates “expand from a center and count palindromes,” making the odd/even structure clear and avoiding inlined duplicate while-loops. A tidy refactoring of the expand-around-center pattern.


        # ----- Edge Cases -----

        # Empty string -> The loop never runs; returns 0.

        # Single character -> Odd expand at i=0 counts 1; even expand counts 0 → returns 1.

        # All same characters ("aaa") -> Every center expands maximally → counts all nested palindromes (for "aaa": “a”×3, “aa”×2, “aaa”×1 = 6).

        # No repeats ("abc") -> Only single chars are palindromes → each odd expand counts 1, even counts 0 → returns 3 (= n).

        # Even-length palindromes ("aa") -> The even center catches "aa" → counts the 2 single chars + 1 "aa" = 3.

        # Full-string palindrome ("aba") -> Counts “a”,”b”,”a” (3 singles) + “aba” (1) = 4.






