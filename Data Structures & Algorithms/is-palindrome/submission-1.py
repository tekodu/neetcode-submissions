class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_chars = []
        
        for char in s:
            if char.isalnum():
                char = char.lower()
                clean_chars.append(char)
        
        return clean_chars == clean_chars[::-1]
