class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # One set per column — tracks digits seen so far in that column
        cols = defaultdict(set)
        # One set per row — tracks digits seen so far in that row
        rows = defaultdict(set)
        # One set per 3×3 box — tracks digits seen so far in that box
        box = defaultdict(set)
        
        # Scan Every Cell
        for r in range(9):
            for c in range(9):
                # Skip empty cells — "." means unfilled
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in box[(r//3, c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                box[(r//3, c//3)].add(board[r][c])
        
        return True

        # TC: O(1) -> 
        # SC: O(1) -> 
