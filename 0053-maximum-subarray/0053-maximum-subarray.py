class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, currSum = nums[0], 0
        
        # iterate through our nums array
        for n in nums:
            
            # if at any point our current sum is negative, set our current sum back to zero
            if currSum < 0:
                currSum = 0
                
            # add the number to our currSum
            currSum += n
            
            # set max subarray to either the currSum or keep itself
            maxSub = max(maxSub, currSum)
            
        return maxSub 
            
        