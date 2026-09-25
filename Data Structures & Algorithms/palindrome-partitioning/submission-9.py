class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # This is to collect all valid partitions (each a list of palindromic pieces)
        result = []
        # The current partition being built
        part = []

        # Backtracking helper: start = where the next piece begins
        def backtrack(start):
            # If start reached the end, the whole string is partitioned
            if start == len(s):
                # Record a copy of the current partition and return
                result.append(part.copy())
                return 
            
            # Try every possible end index for the next piece (s[start..end])
            for end in range(start, len(s)):
                # Only proceed if that piece is a palindrome (the constraint)
                if self.isPalindrome(s, start, end):
                    # Choose: add the palindromic piece s[start..end]
                    part.append(s[start:end + 1])
                    # Recurse to partition the rest, starting after this piece (end + 1)
                    backtrack(end + 1)
                    # Un-choose (backtrack): remove the piece
                    part.pop()
        
        # Start partitioning from index 0
        backtrack(0)
        # Return all partitions
        return result
    
    # Helper: checks if s[l..r] (inclusive) is a palindrome, using two pointers
    def isPalindrome(self, s, left, right):
        # Move the two pointers toward each other while they haven't crossed
        while left < right:
            # If the outer characters differ, it's not a palindrome
            if s[left] != s[right]:
                return False
            # Advance the left and right pointers inward
            left += 1
            right -= 1
        # Pointers met/crossed with no mismatch → it's a palindrome
        return True
    

    # TC: O(n · 2ⁿ) -> there are up to 2^(n-1) ways to partition a string of length n (each of the n-1 gaps between characters is either a cut or not) → O(2ⁿ) possible partitions. Each cut involves an O(n) palindrome check plus O(n) copies. The palindrome check prunes many branches (non-palindromic cuts are abandoned early), so it's faster in practice, but the worst case (e.g. s = "aaaa...") has exponentially many valid partitions → O(n·2ⁿ).
    # SC: O(n) -> recursion depth plus the running partition.


    # Solution Description: We split the string into pieces, one piece at a time, from left to right. At each step, the "choice" is how long the next piece is — we try every prefix starting at the current position. The constraint: a prefix can only become a piece if it's a palindrome. Concretely, from position start, we try each substring s[start:end] for increasing end. If that substring is a palindrome, we add it to the current partition and recurse from end (the start of the next piece). When start reaches the end of the string, we've partitioned the whole thing into palindromes — record the partition. The backtracking undoes each choice so we can try a different cut length.


    # ----- Deep Dive -----

    # The choice is a CUT LENGTH, not an element -> Previous problems picked an element from an array. Here, the "choice" is HOW LONG the next piece is — i.e. where to place the cut. From position `start`, the next piece can be: s[start:start+1] (length 1), s[start:start+2] (length 2) .... s[start:len(s)] (the whole rest). The `end` loop enumerates all these prefix lengths. Each valid (palindromic) choice carves off a piece and recurses on what remains.

    # Why the palindrome check gates the choice -> Not every prefix is a legal piece — only PALINDROMIC ones. The check gates which cuts we're allowed to make. This is constraint-gated backtracking (like Generate Parentheses' validity rules): we only recurse into choices that satisfy the constraint. Invalid cuts are never explored → pruning.

    # Why s[start:end + 1] — the inclusive slice -> uses + 1 because end is the inclusive last index (matching isPalindrome(start, end)), but Python slicing is exclusive of the stop index. Adding 1 includes the character at end. Mismatching this (using s[start:end]) would drop the last character.

    # Why recurse from end + 1 -> After carving off the piece s[start..end], the NEXT piece begins right after it — at index end + 1. Ex: s = "aab", took piece "aa" (start=0, end=1) → the rest to partition is "b", starting at index 2 = end + 1. Recursing from end + 1 means "now partition the remaining suffix." The start index marches forward through the string as pieces are carved off. When start eventually reaches len(s), the whole string is consumed → done.

    # Why the base case is start == len(s) -> The base case start == len(s) fires when the whole string has been consumed into palindromic pieces — the current part is a complete valid partition. Each path from start=0 to start=len(s) represents one full partitioning, with every piece guaranteed palindromic by the gate at each cut.







        