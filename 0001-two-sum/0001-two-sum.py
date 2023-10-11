class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. create an empty hashmap
        2. loop through my numbers using the index of number
            - subtract the number at the idx from the target and store it in a variable
            - check if that variable is already in the hashmap
                - return our current idx and the value of the variable in the hashmap
                - if not in hashmap
                    - add the number and the idx to the hashmap
        
        """
        
        hashmap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        