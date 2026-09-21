class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or
                board[r][c] != word[i]):
                return False
            
            board[r][c] = "#"

            result = (backtrack(r + 1, c, i + 1) or
                      backtrack(r - 1, c, i + 1) or
                      backtrack(r, c + 1, i + 1) or
                      backtrack(r, c - 1, i + 1))
            
            board[r][c] = word[i]

            return result
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False


        # TC: 
        # SC: 


        # Solution Descriptions: We need to find a path through the grid whose letters spell word, moving only to adjacent cells and never reusing a cell. This is a DFS from each possible starting cell, with backtracking to undo failed paths. For each cell in the grid, we try starting the word there. The DFS matches one letter at a time: if the current cell holds the letter we need, we mark it used and recurse into its four neighbors to match the next letter. If we match all letters, we've found the word. If a path dead-ends, we unmark the cell (backtrack) so it can be part of a different path. The visited-marking is the grid analogue of the used array from Permutations — but here we can cleverly mark cells directly in the board to save space.


        # ----- Deep Dive -----

        # 






