class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = [i for i in s.lower() if i.isalnum()]
        return cleanStr == cleanStr[::-1]
        
        