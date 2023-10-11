class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. create a function check if the chars are alphanumeric
        2. intiate a left pointer and a right pointer
        3. at each increment/decrement of the pointers, check to see if the char is alphanumeric and if they're equal
            - not equal return false
            - not alphanumeric, increment/decrement the pointers
        """
        
        l, r = 0, (len(s) - 1)
        
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
            
        return True
        
    def isAlphaNum(self, c):
        return  ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9")
        
        