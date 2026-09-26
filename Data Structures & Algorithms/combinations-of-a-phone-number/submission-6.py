class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Guard: if the input is empty, return an empty list (no combinations for no digits)
        if not digits:
            return []

        # digit→letters lookup map
        digitToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # This is to collect all completed combinations
        result = []
        # The current combination being built (a list of letters)
        combo = []

        # Helper: i = index of the digit we're currently choosing a letter for
        def backtrack(i):
            # If i has reached the end, we've chosen a letter for every digit
            if i == len(digits):
                # Join the letters into a string and record it
                result.append("".join(combo.copy()))
                return
            
            # Loop over each letter that the current digit (digits[i]) maps to
            for letter in digitToLetter[digits[i]]:
                # Choose: append this letter to the combination
                combo.append(letter)
                # Recurse to choose a letter for the next digit (i + 1)
                backtrack(i + 1)
                # Un-choose (backtrack): remove the letter
                combo.pop()
        
        # Start choosing from the first digit (index 0)
        backtrack(0)
        # Return all combinations
        return result


        # TC: O(n · 4ⁿ) -> each digit contributes up to 4 choices, across n digits → up to 4ⁿ combinations (the product of the per-digit option counts). For each complete combination, "".join(combo) costs O(n). 4ⁿ combinations × O(n) join each = O(n · 4ⁿ).
        # SC: O(n) -> recursion depth plus the running combination (the map is constant size)

        # Solution Description: Each digit maps to a few letters, and we build combinations by choosing one letter per digit, in order. With digits "23", digit 2 offers abc and digit 3 offers def, so we form ad, ae, af, bd, ... — every way of picking one letter from each digit's set. We process digits left to right, tracked by an index i. At digit i, we loop over its letters; for each, we append it to the current combination and recurse to digit i + 1. When i reaches the end (we've chosen a letter for every digit), the combination is complete. The backtracking undoes each letter so we can try the next one. There's no constraint to check and no reuse concern — just a clean product of choices.


        # ----- Deep Dive -----

        # One choice per position — the simplest backtracking shape -> Each POSITION (digit) has a fixed set of options (its letters). We pick exactly ONE option per position, then move to the next position. digit 0's letters → choose one → digit 1's letters → choose one → ... There's no start index (we always advance i+1 — every digit is used exactly once, in order) and no used array (each position has its OWN option set, so no cross-position conflict). It's just: "for each position, try each option, recurse to the next position." The purest form of the choose/explore/un-choose rhythm.

        # Why i + 1 and no start index -> We always move to the NEXT digit (i+1) because each digit contributes exactly one letter, in positional order. We're not choosing WHICH digit to use next (they're used in order 0,1,2...) → no start index needed (that was for skipping/ordering array elements). We're not avoiding reuse of a shared pool (each digit has its own letters) → no used array needed. Just: digit 0, then digit 1, then digit 2... i+1 marches straight through.

        # Why the empty-input guard matters -> The empty-input guard prevents returning [""] instead of []. Without it, backtrack(0) would immediately record "".join([]) = "", giving one bogus empty-string combination. For zero digits, the correct answer is zero combinations ([]), so we short-circuit before the recursion.

        # Why "".join(combo) and the base case at i == len(digits) -> he base case i == len(digits) fires when every digit has a chosen letter — the combination is done. We "".join(combo) to turn the list of letters into a string (the required output format). Using a list + join (rather than string concatenation) keeps append/pop O(1); the join is the string analogue of subset.copy() — a frozen snapshot.
 








        