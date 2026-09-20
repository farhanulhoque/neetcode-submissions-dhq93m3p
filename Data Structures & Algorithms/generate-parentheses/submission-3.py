class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # This is to collect all valid parentheses strings
        result = []
        # This is the string being built (a list of chars, joined at the end)
        stack = []

        # Helper: openP = opens used so far, closeP = closes used so far
        def backtrack(openP, closeP):
            # Success: used all n opens and all n closes → string is complete and valid → record it
            if openP == closeP == n:
                result.append("".join(stack.copy()))
                return
            
            # Rule 1: can we add "("? Only if we haven't used all n opens
            if openP < n:
                # Add "(", recurse (one more open), then undo
                stack.append("(")
                backtrack(openP + 1, closeP)
                stack.pop()
            
            # Rule 2: can we add ")"? Only if there's an unmatched open
            if closeP < openP:
                # Add ")", recurse (one more close), then undo
                stack.append(")")
                backtrack(openP, closeP + 1)
                stack.pop()
        
        # Start with 0 opens, 0 closes
        backtrack(0, 0)
        # Return all valid strings
        return result

        
        # TC: O(4ⁿ / √n) -> The number of valid parentheses strings is the nth Catalan number, C(n) ≈ 4ⁿ / (n^1.5 · √π). For each valid string we do "".join(stack), costing O(n). So total ≈ O(n · 4ⁿ / n^1.5) = O(4ⁿ / √n). The pruning is what keeps us near the Catalan count rather than 2^(2n): we only build valid strings, not all possible ( / ) strings.
        # SC: O(n) ->  recursion depth = 2n (one frame per character placed) → O(n) stack. The `stack` list holds at most 2n characters → O(n). O(n) extra space, not counting stored results.
        
        # What's a Catalan Number? -> A Catalan number is the nth term of the sequence 1, 1, 2, 5, 14, 42, .... It counts the valid parentheses strings for n pairs exactly: n=2 gives C(2)=2 strings, n=3 gives C(3)=5, and so on. So when we say "there are Catalan-many valid strings," we mean this specific, well-studied count. The nth Catalan number is C(n) = (2n)! / ((n+1)! · n!), which grows roughly like 4ⁿ / n^1.5. The Catalan numbers count a whole family of "nesting/balancing" structures — valid parentheses, the number of distinct binary search trees with n nodes (relevant to your Trees work), polygon triangulations, and more. Whenever you count balanced or non-crossing arrangements, Catalan numbers tend to appear.


        # Solution Description: Unlike the previous problems (which picked elements from an array), here each step chooses one of two characters: ( or ). The art is knowing when each is allowed, so we only ever build valid strings. Two rules govern the choices, tracked by counts of open and close parentheses used so far: 1. We can add ( as long as we haven't used all n opens (open < n). 2. We can add ) only if it would have a matching open before it (close < open). We build the string character by character, applying these rules to decide which additions are legal. When the string reaches length 2n (all n pairs placed), it's a complete valid string. The constraints prune invalid paths before we explore them — so we never generate a malformed string in the first place.


        # ----- Deep Dive -----

        # The choice is a CHARACTER, not an array element -> There's no input array to iterate. The "choices" are the two fixed characters: "(" and ")". At each step we have (up to) TWO options, each gated by a rule: 1. add "(" — if allowed by Rule 1, 2. add ")" — if allowed by Rule 2. Instead of a for loop over array indices, we have two if-blocks, one per possible character. Same choose/explore/un-choose rhythm, different choices.

        # Rule 1 — why open < n gates adding "(" -> We have exactly n pairs → exactly n opening parens to place. We may add "(" only while we still have opens left to use: openN < n → we've used fewer than n opens → adding another is allowed. openN == n → all opens placed → adding more would exceed n pairs → forbidden. 

        # Rule 2 — why close < open gates adding ")" -> A ")" is only valid if there's an unmatched "(" before it to close. closeN < openN means: we've placed FEWER closes than opens → there's at least one open paren still "waiting" to be closed → adding ")" is valid. This enforces the well-formedness invariant — closes never exceed opens at any point — at every step. Because of it, we never construct an invalid string in the first place; validity is built in, not checked afterward.

        # Why the constraints are PRUNING -> The two if-conditions aren't just correctness checks — they're PRUNING. A naive approach would generate ALL 2^(2n) strings of ( and ), then filter for valid ones. Most would be invalid → huge waste. The rules prevent us from ever ENTERING an invalid branch. We explore ONLY valid partial strings → far fewer paths. This is pruning at its purest: the constraints shape the search tree so we visit close to only the valid answers (the Catalan number of them).

        # Why openN == closeN == n is the completion check -> openN == closeN == n fires when all n opens and all n closes are placed — a complete, balanced string of length 2n. The chained comparison checks both equal n. (Equivalently, you could check len(stack) == 2n.) The rules guarantee that reaching n opens and n closes yields a valid string, so recording here is safe.

        # openN + 1 and closeN + 1 -> They track the counts as they change down the recursion — they're how each recursive call knows "how many opens and closes have been placed so far." When we add a character, the corresponding count goes up by one — and we pass the updated count to the next call. The +1 communicates the new state DOWN to the next level: "I've now placed one more open (or close) — here's the updated count."










