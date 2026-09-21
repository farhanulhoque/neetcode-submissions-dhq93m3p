class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # visited-set variant (if mutating the board isn't allowed)

        rows, cols = len(board), len(board[0])
        visited = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                board[r][c] != word[i]):
                return False
            
            visited.add((r, c))

            result = (backtrack(r + 1, c, i + 1) or
                      backtrack(r - 1, c, i + 1) or
                      backtrack(r, c + 1, i + 1) or
                      backtrack(r, c - 1, i + 1))
            visited.remove((r, c))

            return result
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False