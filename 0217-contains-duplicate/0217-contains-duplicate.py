class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        # loop through my numbers
        for n in nums:
            # compare the numbers to the set
            # if the number is already in the set- its a duplicate- return true
            if n in s:
                return True
            # if its not in the set, we'll add it to the set
            s.add(n)
        #return false
        return False
        