class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Grab dimensions — COLS is the divisor for all index math
        ROWS, COLS = len(matrix), len(matrix[0])
        # Search space is the flat index range [0, m·n - 1] — inclusive on both ends. Total cells = ROWS * COLS, Valid flat indices = 0 .. (ROWS*COLS - 1). Forgetting the -1 lets mid reach ROWS*COLS, producing row = ROWS → matrix[ROWS] → IndexError. It's the inclusive-bound convention from the previous problem: r must be the last valid index, which pairs with while l <= r.
        left, right = 0, (ROWS * COLS) - 1

        while left <= right:
            # Find Overflow-safe midpoint of the flat range
            mid = left + (right - left) // 2
            # Convert flat index → 2-D coordinates: // gives the row, % gives the column. row = mid // COLS  → "how many COMPLETE rows fit before me?". col = mid % COLS → "how far into my row am I?"
            row, col = mid // COLS, mid % COLS
            # Fetch the actual value at that cell
            val = matrix[row][col]

            # Found it
            if val == target:
                return True
            # Too large → target is earlier → discard right half and mid
            elif val > target:
                right = mid - 1
            # Too small → target is later in the flattened order → discard left half and mid
            else:
                left = mid + 1
        # Pointers crossed — target isn't in the matrix
        return False

        # TC: O(log(m . n)) -> The search space is m·n virtual indices, halved every iteration → log₂(m·n) steps. Each step does O(1) work (one division, one modulo, one comparison)
        # SC: O(1) -> Only l, r, mid, row, col — we never materialize the flattened array. That's the whole point of "virtual" flattening

        # Solution Description: The two constraints together mean the matrix is really one sorted array wrapped into rows. Reading it left-to-right, top-to-bottom gives a fully ascending sequence. So we binary search over the virtual flat index range [0, m·n - 1] as if the matrix were a flat array, and convert each midpoint into a real (row, col) on the fly: row = mid // n, col = mid % n. Everything else is textbook binary search — compare, discard half, repeat.
        
        # A 1000×1000 matrix has a million cells — this finds any target in ~20 comparisons.
        # Why the two constraints let us flatten at all -> Each row is sorted ascending - within a row, values increase. First of row i+1 > last of row i - ACROSS rows, values increase. Together these mean reading row-by-row gives one globally sorted sequence
        # The index conversion — mid // COLS and mid % COLS -> The index conversion — mid // COLS and mid % COLS. Integer division groups indices into buckets, modulo gives the position within the bucket.
        # Why COLS (not ROWS) is the divisor -> Reading order fills a ROW at a time, and a row contains COLS cells. So COLS is the "stride" — how many flat indices you advance to move down exactly one row. You divide by the length of the thing you're chunking into. Rows have length COLS, so divide by COLS

