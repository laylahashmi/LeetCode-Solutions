class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. outer loop will traverse the list start at the first position
        2. inner loop will traverse starting at the second position
        3. add the numbers at the two indices to see if they equal the target
        4. if they do, we'll push the two numbers to our result array
        5. if they don't, we'll move to the next indices
        """
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        