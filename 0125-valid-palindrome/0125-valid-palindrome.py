class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. use regex to clean string
        2. convert to lowercase only
        3. reverse string
        4. compare the clean string and the reversed string
        """
        cleanStr = re.sub("[^a-zA-Z0-9]", "", s).lower()
        return cleanStr == cleanStr[::-1]