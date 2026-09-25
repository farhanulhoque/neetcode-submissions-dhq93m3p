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
    

    # TC: 
    # SC: 


    # Solution Description: We split the string into pieces, one piece at a time, from left to right. At each step, the "choice" is how long the next piece is — we try every prefix starting at the current position. The constraint: a prefix can only become a piece if it's a palindrome. Concretely, from position start, we try each substring s[start:end] for increasing end. If that substring is a palindrome, we add it to the current partition and recurse from end (the start of the next piece). When start reaches the end of the string, we've partitioned the whole thing into palindromes — record the partition. The backtracking undoes each choice so we can try a different cut length.


    # ----- Deep Dive -----

    # The choice is a CUT LENGTH, not an element -> 





        