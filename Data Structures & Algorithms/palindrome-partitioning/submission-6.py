class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def backtrack(start):
            if start == len(s):
                result.append(part.copy())
                return
            
            for end in range(start, len(s)):
                if self.isPalindrome(s, start, end):
                    part.append(s[start: end + 1])
                    backtrack(end + 1)
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