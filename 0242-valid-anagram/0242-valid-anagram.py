class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. check if length of strings are equal
            - create two empty hashmaps for each string
            - loop through the strings
            - add the letter at each idx as the key and the occurence of each letter as the value
            - if the two hashmaps equal each other, return true
        2. Return false
        """
        
        countS, countT = {}, {}
        
        if len(s) == len(t):
            for i in range(len(s)):
                countS[s[i]] = countS.get(s[i], 0) + 1
                countT[t[i]] = countT.get(t[i], 0) + 1
                
            return countS == countT
        
        return False