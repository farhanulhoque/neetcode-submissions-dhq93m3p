class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Store the grid dimensions (rows and columns) for boundary checks
        rows, cols = len(board), len(board[0])

        # Helper: (r, c) = current cell, i = index of the letter in word we're trying to match
        def backtrack(r, c, i):
            # If i has reached the word's length, every letter matched → the word is fully found. Return True.
            if i == len(word):
                return True
            
            # Boundary check: the row is above the grid or below it, the column is left of the grid or right of it, Mismatch check: this cell's letter isn't the one we need (word[i]). If any of those failed, this path is invalid → return False
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or
                board[r][c] != word[i]):
                return False
            
            # Mark the current cell as used by overwriting it with "#"
            board[r][c] = "#"

            # Try moving down/up/right/left to match the next letter (i + 1)
            result = (backtrack(r + 1, c, i + 1) or
                      backtrack(r - 1, c, i + 1) or
                      backtrack(r, c + 1, i + 1) or
                      backtrack(r, c - 1, i + 1))
            
            # Backtrack: restore the cell's original letter (word[i], which we know matched)
            board[r][c] = word[i]

            # Return whether any of the four directions found the word
            return result
        
        # Loop over every (row, col) cell as a possible starting point. Try to find the word starting from this cell. If found from any start, return True immediately
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
                    
        # No starting cell worked → the word isn't present. Return False
        return False


        # TC: O(m . k . 4^L) -> We try starting the DFS from each of the m·k cells → the outer loops. From each start, the DFS explores up to 4 directions at each of L steps → up to 4^L paths per start (each of the L letters branches ~4 ways). In practice, the mismatch check prunes most paths almost immediately, so it's far faster than the worst case. m = rows, k = columns, L = length of word.
        # SC: O(L) -> The recursion depth is at most L. We mark cells IN the board (no separate visited structure) → O(1) extra for marking. If a separate visited set were used instead of marking the board, it'd add O(m·k) space — the in-board marking avoids that.


        # Solution Descriptions: We need to find a path through the grid whose letters spell word, moving only to adjacent cells and never reusing a cell. This is a DFS from each possible starting cell, with backtracking to undo failed paths. For each cell in the grid, we try starting the word there. The DFS matches one letter at a time: if the current cell holds the letter we need, we mark it used and recurse into its four neighbors to match the next letter. If we match all letters, we've found the word. If a path dead-ends, we unmark the cell (backtrack) so it can be part of a different path. The visited-marking is the grid analogue of the used array from Permutations — but here we can cleverly mark cells directly in the board to save space.


        # ----- Deep Dive -----

        # Marking the cell in the board itself (board[r][c] = "#") -> temporarily OVERWRITE the cell with a sentinel ("#") that can't match any letter. While the cell holds "#", any path that revisits it will FAIL the "board[r][c] != word[i]" check → effectively "visited." board[r][c] = "#"  → cell is now "in use" for the current path, board[r][c] = word[i] → restore it after exploring (backtrack). This saves O(m·k) space for a separate visited structure — we reuse the board itself as the visited-marker.

        # Why restore word[i] and not "#" (the backtrack) -> When we entered this cell, we KNOW it passed the check "board[r][c] == word[i]". So the cell's ORIGINAL letter was exactly word[i]. To restore it, we write word[i] back. board[r][c] was word[i] → we set it to "#" → now we restore word[i]. Why restore at all? So OTHER paths (from different starting cells, or the same path exploring a different route) can use this cell again. Without restoring, the "#" would permanently block the cell → later searches fail.

        # Why the four recursive calls use "or" -> We're SEARCHING for a path (does ANY direction lead to success?). "or" returns True as soon as ANY direction succeeds → short-circuits. Short-circuit efficiency: the moment one direction finds the word, we stop exploring the rest — no wasted work.

        # The combined base cases — why order matters -> The success check MUST come before the boundary/mismatch check. When i == len(word), we've matched ALL letters — we're "done" and should return True WITHOUT looking at board[r][c] (which might be out of bounds or irrelevant at this point). If we checked bounds first, we might return False on a valid complete match, or try to access board[r][c] when i is already past the word. Order: "did we finish the word?" → yes: True. Only if NOT finished do we check "is this cell valid and matching?" The bounds checks come BEFORE board[r][c] access, so we never index out of bounds (short-circuit: if r<0 is True, we never evaluate board[r][c]).

        # Why we try every cell as a starting point -> The word could start ANYWHERE in the grid. We don't know which cell holds the first letter (there may be several), so we try starting the DFS from EVERY cell. backtrack(r, c, 0) → "can we spell the word starting here (letter index 0)?" As soon as ANY starting cell spells the word → return True. If no cell works → return False.








