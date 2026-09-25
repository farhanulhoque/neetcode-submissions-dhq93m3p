class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def backtrack(start):
            if start == len(s):
                result.append(part.copy())
                return
            
            for i in range(start, len(s)):
                if self.isPalindrome(s, start, i):
                    part.append(s[start:i + 1])
                    backtrack(i + 1)
                    part.pop()
        backtrack(0)
        return result
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        return True
    
