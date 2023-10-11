class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        1. compare the lengths of the two str
        2. create hashmaps for each string and create key, value pairs 
            -key will be the letter in the strings and value will be the occurence of the letter in the strings
        3. compare the two hashmaps and make sure each key, value pair is the same
        '''
        
        if len(s) == len(t):
            countS, countT = {}, {}
            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
            return countS == countT
        
        return False
        