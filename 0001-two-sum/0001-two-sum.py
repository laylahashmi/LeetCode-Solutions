class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. create an empty hashmap
        2. loop through my nums array and create key and value pairs
            - find the complement (target - number at a certain index)
            - check and see if the complement already exists in the hashmap
                - return [number at that index and the complement]
            - add the complement to the hashmap
        """
        
        hashmap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
            
        