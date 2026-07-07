class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize the pointers
        left, right = 0, len(s) - 1

        while left < right:
            # If the left character is not alphanumeric, skip it. Move pointer rightward past the invalid character
            while left < right and not self.isAlphaNum(s[left]):
                left += 1
            # If the right character is not alphanumeric, skip it. Move pointer leftward past the invalid character
            while left  < right and not self.isAlphaNum(s[right]):
                right -= 1
            # Compare both characters case-insensitively. If Mismatch found → not a palindrome → return False
            if s[left].lower() != s[right].lower():
                return False
            # Characters matched → move both "left" and "right" pointers inward
            left += 1
            right -= 1
        # Pointers crossed with no mismatches → valid palindrome
        return True
    
    def isAlphaNum(self, char):
        # Check if char is an uppercase letter — ASCII range 65 to 90 or lowercase letter — ASCII range 97 to 122 or a digit — ASCII range 48 to 57
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))
    

    # TC: O(n) -> Each character is visited at most once — left and right only ever move inward, never backward
    # SC: O(1) -> No extra data structures - just two integer pointers

    # Solution Description: Place one pointer left at the start and one pointer right at the end of the string. Move them inward toward each other, skipping any non-alphanumeric characters using a custom helper. At each valid pair, compare the characters case-insensitively. If they ever mismatch → not a palindrome. If the pointers cross without a mismatch → it is a palindrome.

