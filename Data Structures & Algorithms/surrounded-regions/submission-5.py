class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Multi-Source DFS

        # Guard: if the board is empty, nothing to do, return
        if not board:
            return
        
        # Store the board dimensions
        rows, cols = len(board), len(board[0])

        # DFS helper that marks a connected safe region from (r, c)
        def dfs(r, c):
            # Boundary check: row or column out of the board. Only flood 'O' cells — stop at 'X' or already-marked 'T'
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != "O"):
                # If any check fails, stop this branch
                return
            
            # Mark this 'O' as 'T' (temporarily safe)
            board[r][c] = "T"

            # Flood the neighbors (below, above, right, left)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # For each row, flood from the left and right columns
        for r in range(rows):
            # DFS from the left-edge cell
            dfs(r, 0)
            # DFS from the right-edge cell
            dfs(r, cols - 1)
        
        # For each column, flood from the top and bottom rows
        for c in range(cols):
            # DFS from the top-edge cell
            dfs(0, c)
            # DFS from the bottom-edge cell
            dfs(rows - 1, c)
        
        # Scan every cell
        for r in range(rows):
            for c in range(cols):
                # A remaining 'O' is surrounded (never reached from border), capture it → 'X'
                if board[r][c] == "O":
                    board[r][c] = "X"
                # A 'T' is safe (border-connected), restore it → 'O'
                elif board[r][c] == "T":
                    board[r][c] = "O"


        # TC: O(m . n) -> the border-flooding DFS visits each 'O' cell at most once (marked 'T' on first visit → the "!= 'O'" check skips it after) → O(m·n) total across all floods. The final sweep scans all m·n cells once → O(m·n). O(m·n) overall.
        # SC: O(m . n) -> the recursion stack can go O(m·n) deep if the board is one big 'O' region connected to the border → O(m·n). Marking in-place with 'T' avoids a separate visited set.


        # Solution Description: Run DFS from every 'O' on the border, marking all connected 'O's as 'T' (safe). Then do one pass over the board: 'O' → 'X' (surrounded, capture it) and 'T' → 'O' (safe, restore it).


        # ----- Deep Dive -----

        # The reverse approach (mark SAFE cells, capture the rest) -> NAIVE (direct): for each 'O' region, check if ANY cell touches the border. → awkward: you'd flood each region, track whether it hit an edge, then go back and capture it only if it didn't. Fiddly bookkeeping.
                # REVERSE (this): an 'O' survives ONLY if it's connected to the border. So:
                #     1. flood from the border, marking all reachable 'O's as SAFE ('T').
                #     2. everything still 'O' afterward is surrounded → capture it.

                # The flip: instead of "is this region enclosed?" (hard to ask per-region), we ask "which 'O's escape to the border?" (one flood from the edges), then capture the non-escapees. Same answer, far cleaner.
                # Why this works: an 'O' is NOT captured ⟺ it can reach the border through connected 'O's ⟺ the border flood reaches it. The complement (not reached) is exactly the surrounded regions.
        

        # Why only border cells are the sources -> We seed the flood ONLY from the four borders (edge rows and columns), because a region is safe if it touches the edge. The border 'O's are the only guaranteed-safe starting points. dfs from every edge cell → floods inward through connected 'O's → marks the ENTIRE safe region each border 'O' belongs to. Interior 'O's are NOT seeded directly — they only get marked 'T' if the flood REACHES them from a border (i.e., they're connected to the edge). An interior 'O' with no path to the border is never reached → stays 'O' → captured. dfs stops at 'X' and out-of-bounds, so each flood stays within one region.

        # Why a temporary marker 'T' (the three-state trick) -> After the flood, the board has THREE kinds of cells:
                # 'X' → original walls (leave as-is)
                # 'O' → 'O's NOT reached by the flood → SURROUNDED → capture to 'X'
                # 'T' → 'O's reached by the flood → SAFE → restore to 'O'

                # The 'T' marker DISTINGUISHES safe 'O's from surrounded 'O's. Without it, after flooding we couldn't tell which 'O's were safe (we'd have overwritten them to something, or not be able to separate them).
                # The final sweep uses the three states:
                    # 'O' (unmarked) → capture ('X')
                    # 'T' (marked)   → restore ('O')
                    # 'X'            → untouched
                # Why not mark safe cells as 'X' directly? Then they'd look captured — we'd lose the distinction. 'T' is a neutral third state that we resolve at the end.
        

        # Why the final sweep order doesn’t matter -> The sweep processes each cell INDEPENDENTLY based on its current marker — there's no interaction between cells during the sweep. Since each cell's new value depends only on ITS OWN marker (not neighbors), the sweep can go in any order. No flooding, no dependencies — just a direct per-cell relabeling. This is why the two-phase structure (flood THEN sweep) is clean: the flood sets the markers; the sweep reads them cell-by-cell with no ordering concerns.


        # ----- Edge Cases -----

        # 






