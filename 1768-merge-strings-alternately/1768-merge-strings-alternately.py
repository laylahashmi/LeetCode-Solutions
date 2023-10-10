class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0 #index 
        
        # while the index is less than the length of either word
        while i < len(word1) or i < len(word2):
            # if the index is less than the length of first word, add the letter at that index to our result
            if i < len(word1):
                result.append(word1[i])
            
            # if the index is less than the length of second word, add the letter at that index to our result
            if i < len(word2):
                result.append(word2[i])
            
            # increment the index by 1
            i += 1
            
        return "".join(result)
    