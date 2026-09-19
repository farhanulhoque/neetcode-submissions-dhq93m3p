class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        combo = []

        def backtrack(start, total):
            if total == target:
                result.append(combo.copy())
                return
            
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combo.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                combo.pop()
            
        backtrack(0, 0)
        return result