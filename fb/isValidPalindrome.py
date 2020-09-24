# Solution to LC: 680 Valid Palindrome II

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if self.isPalindrome(s, left + 1, right):
                    return True
                if self.isPalindrome(s, left, right - 1):
                    return True
                return False
        return True
                
        
    
    
    def isPalindrome(self, s: str, left: int, right:int) -> bool:
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                return False
        return True
            