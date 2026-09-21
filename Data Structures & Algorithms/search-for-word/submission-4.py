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


        # TC: 
        # SC: 


        # Solution Descriptions: We need to find a path through the grid whose letters spell word, moving only to adjacent cells and never reusing a cell. This is a DFS from each possible starting cell, with backtracking to undo failed paths. For each cell in the grid, we try starting the word there. The DFS matches one letter at a time: if the current cell holds the letter we need, we mark it used and recurse into its four neighbors to match the next letter. If we match all letters, we've found the word. If a path dead-ends, we unmark the cell (backtrack) so it can be part of a different path. The visited-marking is the grid analogue of the used array from Permutations — but here we can cleverly mark cells directly in the board to save space.


        # ----- Deep Dive -----

        # 






