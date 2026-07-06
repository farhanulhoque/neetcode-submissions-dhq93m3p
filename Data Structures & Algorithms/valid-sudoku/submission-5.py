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
                # Check if this digit already exists in this row, col, or box
                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in box[(r//3, c//3)]):
                    # If any check fails → duplicate found → board is invalid
                    return False

                # Add the digit to this row's, col's, and box's set
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                box[(r//3, c//3)].add(board[r][c])
        
        # Survived all checks → board is valid
        return True

        # TC: O(1) -> Always exactly 9×9=81 cells — fixed input size
        # SC: O(1) -> At most 9 digits accros 9 rows + 9 cols + 9 boxes = fixed size sets

        # Since the board is always 9×9, everything is technically constant. If we generalized to an n×n board it would be O(n²) time and space.
        