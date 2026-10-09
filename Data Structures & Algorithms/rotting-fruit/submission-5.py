class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS (multi-source)

        # Store the grid dimensions
        rows, cols = len(grid), len(grid[0])
        # The BFS queue
        q = deque()
        # Counter for how many fresh oranges exist
        fresh = 0

        # Scan every cell. 
        for r in range(rows):
            for c in range(cols):
                # If this cell is a fresh orange (1), count it. 
                if grid[r][c] == 1:
                    fresh += 1
                # Else if it's a rotten orange (2),seed the queue with it (all rotten are sources)
                elif grid[r][c] == 2:
                    q.append((r, c))

        # Minutes elapsed (the answer)
        minutes = 0
        
        # BFS while there are rotten oranges to spread from and fresh oranges remain
        while q and fresh > 0:
            # Level-freezing: process exactly the current layer (one minute's worth)
            for i in range(len(q)):
                # Dequeue a rotten orange
                row, col = q.popleft()
                # Check each of its four neighbors
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    # Compute the neighbor's coordinates
                    nr, nc = row + dr, col + dc
                    # Bounds check. Only rot a fresh neighbor (1)
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        # Rot it (set to 2)
                        grid[nr][nc] = 2
                        # Decrement the fresh count
                        fresh -= 1
                        # Enqueue the newly-rotten orange (it spreads next minute)
                        q.append((nr, nc))
            # One full level processed → one minute elapsed
            minutes += 1
        
        # If no fresh remain, return the minutes; otherwise -1 (some unreachable)
        return minutes if fresh == 0 else -1


        # TC: O(m . n) -> the initial scan to count fresh and seed rotten visits all m·n cells → O(m·n). The BFS: each orange is enqueued at most once (rotted on first reach → becomes 2 → never re-enqueued), and each dequeue checks 4 neighbors (O(1)). So the BFS is O(m·k) total.
        # SC: O(m . n) -> the queue can hold up to O(m·n) oranges (e.g. if most of the grid is rotten at the start, or a wide BFS frontier). We rot oranges in place (grid doubles as visited) → no extra visited set.


        # Solution Description: Rot spreads one layer per minute from every rotten orange simultaneously — that's multi-source BFS, exactly like Walls and Gates. But here we need two extra things: the number of minutes (how many BFS levels it takes to rot everything) and detection of the impossible case (fresh fruit cut off from all rot). We seed the queue with all initially-rotten oranges and count the fresh ones upfront. Then we BFS level by level (the level-freezing idiom): each level represents one minute of spreading. For each rotten orange processed, we rot its fresh neighbors, enqueue them, and decrement the fresh count. We count a minute for each level that actually rots something. At the end, if any fresh oranges remain (fresh count > 0), some were unreachable → return -1; otherwise return the minutes elapsed.


        # ----- Deep Dive -----

        # Why count LEVELS for minutes (the level-freezing idiom) -> All oranges rotten at the start of a minute rot their neighbors SIMULTANEOUSLY during that minute. So one BFS LEVEL = one minute of spreading. The level-freezing idiom (from Trees!): len(q) captured at the top of the for loop is EXACTLY the oranges rotten going into this minute. We process all of them (rotting their neighbors), and the newly-rotten ones wait in the queue for the NEXT minute.  minute 1: all initially-rotten oranges rot their neighbors (one level), minute 2: those newly-rotten oranges rot THEIR neighbors (next level)....Each while-pass = one minute. minutes += 1 per level → total minutes to rot everything.
            # Why not per-cell distance (like Walls and Gates)? We don't need each cell's distance — we need the TOTAL TIME, which is the number of levels (the last level is when the farthest fresh orange rots). Counting levels gives that directly.


        # Why track the fresh count (detecting the impossible case) -> The problem says: if some fresh fruit can NEVER rot (cut off from all rotten), return -1. We track `fresh`: start with the total fresh count, decrement by 1 each time we rot one. At the end: fresh == 0 → every fresh orange rotted → return minutes, fresh > 0  → some fresh oranges were NEVER reached by the rot → return -1. A fresh orange isolated by empty cells (0) or walls can't be reached by BFS → it's never rotted → fresh stays > 0 → we correctly return -1. The fresh count is how we DETECT completeness without re-scanning the grid.


        # Why the loop condition includes fresh > 0 (avoiding an over-count) -> We stop as soon as there are no fresh oranges left (fresh == 0), even if the queue still has rotten oranges. Why the "fresh > 0" guard matters: without it, we'd process one MORE level after the last fresh orange rots — the newly-rotten oranges from the final minute would be dequeued, find no fresh neighbors, but still trigger minutes += 1 → an EXTRA minute counted.
            # Say the last fresh orange rots in minute 4. Those oranges are enqueued. without "fresh > 0": minute 5 runs, processes them, rots nothing, but minutes becomes 5 → WRONG (should be 4). with "fresh > 0": after minute 4, fresh == 0 → loop exits → minutes = 4
            # The guard stops us the instant all fresh are gone, avoiding a phantom minute.


        # Why multi-source again (all rotten oranges spread together) -> Same multi-source idea as Walls and Gates: ALL initially-rotten oranges rot their neighbors simultaneously each minute, so they're ALL sources. Same multi-source idea as Walls and Gates: ALL initially-rotten oranges rot their neighbors simultaneously each minute, so they're ALL sources. We seed every rotten orange into the queue before the BFS. Then they spread together, level by level. The rot from multiple sources expands as merging ripples — a fresh orange rots as soon as ANY rotten neighbor reaches it. if we seeded only ONE rotten orange, we'd compute the time for IT to rot everything — but other rotten oranges rot things faster. Seeding ALL gives the correct (minimum) time.


        # ----- Edge Cases -----

        # No fresh oranges at all -> fresh starts at 0, so while q and fresh > 0 never runs; minutes stays 0; returns 0. Correct — nothing needs to rot. (This is why the fresh > 0 guard also helps: 0 minutes for an already-done grid.)

        # No rotten oranges, but fresh exist -> The queue is empty, so the loop never runs; fresh > 0 at the end → returns -1. Correct — fresh fruit can never rot with no source.

        # Fresh orange isolated by empty cells -> BFS can't reach it; it's never rotted; fresh stays > 0 → returns -1. The core "impossible" case.

        # All cells empty (0) -> No fresh, no rotten; loop never runs; returns 0. Correct. 

        # Grid already fully rotten -> fresh = 0; loop skipped; returns 0.

        # Single fresh adjacent to single rotten -> Minute 1 rots it, fresh → 0, loop exits; returns 1.

        # The phantom-minute case -> Covered by the fresh > 0 guard — ensures we don't count a minute after the last orange rots.





