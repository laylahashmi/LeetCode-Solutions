class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        1. make an empty dict
        2. loop through my numbers array
            1. number is in the dict, return true
            2. number is not in the dict, add it to the dict with a vaue of 1
        3. no duplicates, answer will be false
        """
        
        res = set()
        
        for i in range(len(nums)):
            if nums[i] in res:
                return True
            res.add(nums[i])
        return False
        
        