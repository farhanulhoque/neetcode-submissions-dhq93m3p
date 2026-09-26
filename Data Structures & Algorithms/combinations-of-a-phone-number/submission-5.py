class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        combo = []

        def backtrack(i):
            if i == len(digits):
                result.append("".join(combo.copy()))
                return
            
            for letter in digitToLetters[digits[i]]:
                combo.append(letter)
                backtrack(i + 1)
                combo.pop()
        
        backtrack(0)
        return result