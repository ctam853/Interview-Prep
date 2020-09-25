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


'''

Idea: Perform normal palindrome check for single string in a helper method, during main function use two pointers and if front and back chars are same move pointers in by 1.
If not then you need to check both deleting from back and deleting from front and see if its a palindrome, if neither are palindromes return False. If you make it out of while 
loop without calling helper then you know its a normal palindome.


'''
            