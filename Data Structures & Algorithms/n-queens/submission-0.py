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
 
        
        # TC: 
        # SC: 


        # Solution Description: We place queens one per row (since each row can hold at most one queen without a horizontal conflict — placing exactly one per row also handles that constraint for free). For each row, we try each column, checking whether placing a queen there is safe from all previously placed queens. The key is O(1) safety checking via three sets: occupied columns, occupied positive diagonals (r + c), and occupied negative diagonals (r - c). A square is safe if its column and both its diagonals are free. When we place a queen, we add its column and diagonals to the sets and recurse to the next row; when we backtrack, we remove them. When we've placed a queen in every row, we've found a solution — we record the board layout.


        # ----- Deep Dive -----

        # 






