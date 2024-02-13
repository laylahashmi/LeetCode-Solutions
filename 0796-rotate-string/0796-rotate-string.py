class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #check is string lengths are equal 
        #check is goal is a substring of s
        return len(s) == len(goal) and goal in s + s
        