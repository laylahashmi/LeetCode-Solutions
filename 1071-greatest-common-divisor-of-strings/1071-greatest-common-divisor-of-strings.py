class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if str1 and str2 do not equal str2 and str1, return an empty string
        if str1 + str2 != str2 + str1:
            return ""
        
        # if the lengths of str1 and str2 are equal and the concatenated strings are equal, return str1 or str2, because either one is gcd
        if len(str1) == len(str2):
            return str1
        
        # if str1 length is greater than str2 length, str1 contains str2 as a prefix, we recurse with the substring of str1 after slicing the prefix that matches str2
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        
        # if str2 length is greater than str1 length, str2 contains str1 as a prefix, we recurse with the substring of str2 after slicing the prefex that match str1
        return self.gcdOfStrings(str1, str2[len(str1):])
        