class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return result
 
        
        # TC: O(n!) —> row 0 has n column choices, row 1 has at most n−1 (a column and diagonals are eliminated), row 2 at most n−2, and so on, giving the factorial branching n × (n−1) × .... Each solution costs O(n²) to copy the board. The constraint sets prune most branches early (dead-ends like row 2 in the trace), so it's much faster in practice, but O(n!) is the worst case
        # SC: O(n²) -> the board is n×n → O(n²). The three sets hold at most n entries each → O(n). recursion depth = n (one frame per row) → O(n). O(n²) total (the board), not counting stored solutions.


        # Solution Description: We place queens one per row (since each row can hold at most one queen without a horizontal conflict — placing exactly one per row also handles that constraint for free). For each row, we try each column, checking whether placing a queen there is safe from all previously placed queens. The key is O(1) safety checking via three sets: occupied columns, occupied positive diagonals (r + c), and occupied negative diagonals (r - c). A square is safe if its column and both its diagonals are free. When we place a queen, we add its column and diagonals to the sets and recurse to the next row; when we backtrack, we remove them. When we've placed a queen in every row, we've found a solution — we record the board layout.


        # ----- Deep Dive -----

        # 






