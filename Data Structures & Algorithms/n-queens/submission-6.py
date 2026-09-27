class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Backtracking + constraint sets

        # This is to collect all solution boards
        result = []
        # The board, initialized to all empty (.) cells
        board = [["."] * n for _ in range(n)]

        # Set of columns that already hold a queen
        cols = set()
        # Set of occupied positive diagonals, keyed by r + c
        posDiag = set()
        # Set of occupied negative diagonals, keyed by r - c
        negDiag = set()

        # Helper: r = the row we're currently placing a queen in
        def backtrack(r):
            # If r reached n, a queen has been placed in every row → a full solution
            if r == n:
                # Build a string-row copy of the board (each row joined into a string)
                copy = ["".join(row) for row in board]
                # Record the completed board layout and return
                result.append(copy)
                return
            
            # Try each column in the current row
            for c in range(n):
                # Check if this square is attacked: same column, or same positive/negative diagonal. If attacked, skip this column
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # Choose: mark the column, positive diagonal, and negative diagonal occupied. Place the queen on the board.
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Recurse to place a queen in the next row
                backtrack(r + 1)

                # Un-choose: free the column, positive diagonal, and negative diagonal. Remove the queen from the board.
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        # Start placing from row 0
        backtrack(0)
        # Return all solutions
        return result
 
        
        # TC: O(n!) —> row 0 has n column choices, row 1 has at most n−1 (a column and diagonals are eliminated), row 2 at most n−2, and so on, giving the factorial branching n × (n−1) × .... Each solution costs O(n²) to copy the board. The constraint sets prune most branches early (dead-ends like row 2 in the trace), so it's much faster in practice, but O(n!) is the worst case
        # SC: O(n²) -> the board is n×n → O(n²). The three sets hold at most n entries each → O(n). recursion depth = n (one frame per row) → O(n). O(n²) total (the board), not counting stored solutions.


        # Solution Description: We place queens one per row (since each row can hold at most one queen without a horizontal conflict — placing exactly one per row also handles that constraint for free). For each row, we try each column, checking whether placing a queen there is safe from all previously placed queens. The key is O(1) safety checking via three sets: occupied columns, occupied positive diagonals (r + c), and occupied negative diagonals (r - c). A square is safe if its column and both its diagonals are free. When we place a queen, we add its column and diagonals to the sets and recurse to the next row; when we backtrack, we remove them. When we've placed a queen in every row, we've found a solution — we record the board layout.


        # ----- Deep Dive -----

        # Why one queen per row (handling horizontal attacks for free) -> By structuring the recursion as "place one queen in row r, then recurse to row r+1", we GUARANTEE at most one queen per row → horizontal attacks are IMPOSSIBLE by construction. We never even check for horizontal (row) conflicts — the structure prevents them. This leaves only THREE things to check: columns, and the two diagonals. Rows are handled for free by the one-queen-per-row recursion.

        # The diagonal-indexing trick (r + c and r - c) -> A chessboard has diagonals in two directions: 1. POSITIVE diagonals (↗ / going up-right): every cell on the SAME diagonal has the SAME value of (r + c), 2. NEGATIVE diagonals (↘ \ going down-right): every cell on the SAME diagonal has the SAME value of (r - c). So to check "is this square on an occupied diagonal?", we just check if (r+c) or (r-c) is in the respective set → O(1)! Moving along a diagonal changes row and column in ways that cancel in the sum (or difference). This lets us represent each diagonal by a single number and check occupancy in O(1) via a set — the key to an efficient solution.

        # Why we don't need a rows set (and the O(1) safety check) -> the one-queen-per-row recursion guarantees the current row is empty (we're placing the FIRST queen in row r). If ANY of the three is occupied → the square is attacked → skip it (continue). If ALL three are free → the square is safe → place the queen. The whole safety check is O(1) — three set lookups. This is what makes N-Queens tractable; a naive "scan all directions" check would be O(n) per square.

        # The paired add/remove for all three sets (backtracking) -> Four pieces of state (cols, posDiag, negDiag, board) are all marked on choose and all unmarked on backtrack. This is the choose/un-choose rhythm scaled up — every structure that records the placement must be restored, or a stale "occupied" marker would wrongly block later valid placements. Symmetric add/remove across all four is essential.

        # Why the board must be copied with "".join -> `board` is ONE mutable 2-D list that we keep modifying (place/remove queens) throughout the recursion. Same copy-vs-reference issue as subset.copy(). If we appended `board` directly, res would hold references to the SAME board, which later gets mutated back to all "." → all solutions would appear empty. "".join(row) does two things: 1. converts each row (a list of chars) into a STRING (the required format), 2. creates a NEW string — a frozen snapshot independent of future mutations. So ["".join(row) for row in board] is a deep-enough copy: new strings, new list, unaffected by later changes to `board`.

        # The r + c / r - c diagonal trick turns an O(n) diagonal scan into an O(1) set lookup. Finding a numeric key that groups related cells (here, diagonals) is a recurring optimization technique.









