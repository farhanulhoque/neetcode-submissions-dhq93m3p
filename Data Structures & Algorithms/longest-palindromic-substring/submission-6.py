class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Expand around center

        # This is to store the longest palindrome found so far (the result string)
        res = ""
        # This is to store the length of the longest palindrome found so far (to compare against new finds)
        resLen = 0

        # Try every index i as a potential center
        for i in range(len(s)):
            # Odd-length palindrome -> center at i
            left, right = i, i
            # Expand while in bounds and the two characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # If this palindrome is longer than the best so far, record the substring s[l..r] and its length
                if (right - left + 1) > resLen:
                    res = s[left: right + 1]
                    resLen = right - left + 1
                # Expand the left and right pointers outward
                left -= 1
                right += 1
            
            # Even-length palindrome -> center between i and i+1
            left, right = i, i + 1
            # Expand while in bounds and the two characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # If this palindrome is longer than the best so far, record the substring s[l..r] and its length
                if (right - left + 1) > resLen:
                    res = s[left: right + 1]
                    resLen = right - left + 1
                # Expand the left and right pointers outward
                left -= 1
                right += 1
        
        # Return the longest palindrome
        return res


        # TC: O(n²) -> we try O(n) centers (n odd centers + n-1 even centers = 2n-1 = O(n)). Each center expands outward up to O(n) times (in the worst case, the whole string, e.g. "aaaa"). O(n) centers × O(n) expansion each = O(n²). O(n²) overall.
        # SC: O(1) -> only a few pointers and the result tracking (l, r, res, resLen). No DP table, no extra data structures (beyond the output). O(1) extra space (not counting the output string).



        # Solution Description: Every palindrome has a center, and it reads the same expanding outward from that center. So we try every possible center and expand left and right as long as the characters match — the longest expansion we find is the answer. Palindromes come in two flavors by center type. Odd-length palindromes (like "aba") have a single-character center. Even-length palindromes (like "abba") have a center between two characters. So for each position, we expand from two kinds of centers: one single char, and one gap between adjacent chars. We track the longest palindrome found across all 2n-1 possible centers.



        # ----- Deep Dive -----

        # Why “expand around center” works (every palindrome has a center) -> A palindrome reads the same forward and backward, which means it's SYMMETRIC around its center. So if you stand at the center and walk outward in both directions, you see matching characters at each step. "racecar": center is 'e'. Expanding: c=c, a=a, r=r → all match → palindrome. 

                # Conversely, EVERY palindrome has a unique center. So if we try every possible center and expand as far as the characters match, we'll find every palindrome — including the longest.

                # for each center, expand while s[l] == s[r] → the widest symmetric span around that center = the longest palindrome centered there. Trying all centers → finding all palindromes → the longest overall.

                # Why centers, not all substrings? There are O(n²) substrings, each taking O(n) to check for palindrome-ness → O(n³) naive. Expanding from O(n) centers, each O(n) nexpansion → O(n²). Centers are the efficient way to enumerate palindromes.
        


        # Why we need BOTH odd and even centers (the two-flavor subtlety) -> Palindromes come in two types by length:

                # ODD-LENGTH (e.g. "aba", "racecar"): has a SINGLE middle character.
                #             center = one char → start l = r = i, expand outward.

                # EVEN-LENGTH (e.g. "abba", "noon"): has NO single middle char — the center
                #             is the GAP between the two middle characters.
                #             center = between i and i+1 → start l = i, r = i+1, expand outward.

                # If we only checked odd centers, we'd MISS all even-length palindromes: "abba": no single character is its center → odd-expansion never finds it. we need the even center (between the two b's) to catch it.

                # So for each index i, we expand TWICE: once as an odd center (l=r=i), once as an even center (l=i, r=i+1). This covers all 2n-1 possible centers (n single-char centers + n-1 between-char centers).
        


        # Why the expansion condition checks bounds AND match -> Three conditions, all required to keep expanding: 

                # l >= 0:        the left pointer is still within the string (not off the left edge).
                # r < len(s):    the right pointer is still within the string (not off the right edge).
                # s[l] == s[r]:  the characters at the two ends still match (still a palindrome).

                # We expand only while ALL three hold. Any failing → stop (this center's palindrome
                # is as wide as it gets).

                #     bounds checks FIRST (short-circuit): if l < 0 or r >= len(s), we don't
                #     evaluate s[l]==s[r] → no index-out-of-bounds error. Order matters.

                #     the match check is what detects the palindrome boundary: once s[l] != s[r],
                #     the symmetry breaks → stop expanding.
        


        # Why r - l + 1 is the palindrome length -> r - l + 1 is the palindrome’s length because l and r are the inclusive endpoint indices — the number of characters from l to r is r - l + 1 (the +1 counts both endpoints). We record s[l:r+1] (the +1 makes Python’s exclusive slice include index r). We update the result only when this length beats the best so far.



        # ----- Edge Cases -----

        # Empty string -> The loop never runs; returns ""

        # Single character -> Odd expansion at i=0 finds a length-1 palindrome → returns that char.

        # All same characters ("aaaa") -> Expansions grow to the full string → returns "aaaa". Both odd and even centers extend fully.

        # No palindrome longer than 1 ("abcd") -> Every expansion stops immediately (no matches beyond single chars) → returns any single char (length 1).

        # Entire string is a palindrome -> The center expansion reaches both ends → returns the whole string.

        # Even-length answer ("cbbd" → "bb") -> The even center between the two bs catches it — would be missed without even-center handling.






