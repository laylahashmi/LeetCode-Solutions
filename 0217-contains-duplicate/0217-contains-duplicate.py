class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        1. create an empty set
        2. loop through my numbers
        3. check if number is in the set
            - if not, add it
            - if it is, return true
        4. loop completes, return false
        """
        
        s = set()
        
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
        