class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Multi-Source DFS

        # Guard: if the grid is empty, return an empty list
        if not heights:
            return []

        # Store the grid dimensions
        rows, cols = len(heights), len(heights[0])
        # Set of cells that can reach the Pacific
        pacific = set()
        # Set of cells that can reach the Atlantic
        atlantic = set()

        # DFS helper: visited = which ocean’s set; prevHeight = the height we came from
        def dfs(r, c, visited, prevHeight):
            # Boundary check: row or column out of the grid. Skip cells already visited in this ocean’s traversal. 	Reverse-flow check: can’t move to a lower cell (water flows downhill, so backward we only go to equal-or-higher).
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r, c) in visited or
                heights[r][c] < prevHeight):
                # If any check fails, stop this branch
                return
            
            # Mark this cell as reachable from the current ocean
            visited.add((r, c))

            # Flow backward (uphill) to the neighbor below, above, right, left
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # For each column, seed the top/bottom row
        for c in range(cols):
            # DFS from the top-row cell into the Pacific set
            dfs(0, c, pacific, heights[0][c])
            # DFS from the bottom-row cell into the Atlantic set
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        
        # For each row, seed the left/right columns
        for r in range(rows):
            # DFS from the left-column cell into the Pacific set
            dfs(r, 0, pacific, heights[r][0])
            # DFS from the right-column cell into the Atlantic set
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        
        # The result list
        result = []
        # Scan every cell. If a cell can reach both oceans (in both sets), add it to the result.
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        
        # Return all cells reachable from both oceans
        return result


        # TC: O(m . n) -> each ocean's reverse-DFS visits each cell at most once (the visited set prevents revisits) → O(m·n) per ocean. Two oceans → 2 · O(m·n) = O(m·n). The final intersection scan is O(m·n). O(m·n) overall.
        # SC: O(m . n) -> the two visited sets hold up to O(m·n) cells each → O(m·n). The recursion stack can go O(m·n) deep worst case → O(m·n).


        # Solution Description: Run DFS backward from each ocean’s borders. For each ocean, seed DFS at its border cells and flow to neighbors of equal or greater height (reverse of downhill), collecting all reachable cells into a set. Do this for Pacific and Atlantic separately, then return the intersection.


        # ----- Deep Dive -----

        # The reverse-flow insight (searching FROM the oceans) -> NAIVE (forward): from each cell, DFS downhill and check if you hit an ocean → m·n cells × O(m·n) search each = O((m·n)²). And you'd search for BOTH oceans from every cell. Very slow. 
                # REVERSE (this): start AT the ocean borders, flow BACKWARD (uphill) into the grid. A cell is reachable backward from the ocean ⟺ water can flow forward from that cell to the ocean. (If you can walk uphill from the ocean to a cell, then water can flow downhill from that cell to the ocean — same path, reversed.) → two grid traversals, O(m·k) each. Fast.
                # The flip: "which cells can reach the ocean?" is hard to ask per-cell, but EASY to answer by flooding backward from the ocean once.
                # Why reverse flow uses "equal or GREATER" height:
                    # forward flow: cell → neighbor if neighbor is LOWER or equal (downhill).
                    # reverse flow: ocean → cell if cell is HIGHER or equal (uphill, backward).
                    # we're tracing the same edges, just in the opposite direction.
        

        # Why the answer is the INTERSECTION of two sets -> We run TWO separate reverse-searches:
                # pacific set  = all cells that can flow to the Pacific (reachable backward from the top row + left column)
                # atlantic set = all cells that can flow to the Atlantic (reachable backward from the bottom row + right column)
                # A cell flows to BOTH oceans ⟺ it's in BOTH sets. → the answer is pacific ∩ atlantic (the intersection).
        

        # Why prevHeight and the heights[r][c] < prevHeight check -> We carry prevHeight = the height of the cell we came FROM. To move backward (uphill) to a new cell, that cell must be AT LEAST as high:
                # heights[r][c] >= prevHeight → we can flow backward here → continue
                # heights[r][c] < prevHeight  → it's lower → water couldn't flow back up → stop
                # When we recurse, we pass the CURRENT cell's height as the next prevHeight — so each step compares against where we just came from, enforcing non-decreasing heights along the backward path. Seeding: border cells are seeded with their OWN height as prevHeight (so they always pass the check — equal to themselves — and get added).
        

        # Why two separate visited sets (one per ocean) -> Each ocean's reverse-search needs its OWN visited set, because a cell can be reachable from the Pacific, the Atlantic, both, or neither — these are INDEPENDENT reachability questions. If we shared one visited set, a cell marked visited by the Pacific search would be skipped by the Atlantic search → we'd miss cells reachable from the Atlantic. Two sets keep the two reachability computations separate, so we correctly determine BOTH memberships, then intersect.


        # ----- Edge Cases -----

        # 







        