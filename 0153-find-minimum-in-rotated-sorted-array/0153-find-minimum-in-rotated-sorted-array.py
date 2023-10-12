class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        1. res which holds our min value
        2. left and right pointers
        3. while left is less than right
            1. if value at left is less than value at right
                -min value will be the min of the res and the value at the left
                - break
            2. find the middle value of the arr
                - set res to min of either res or to the middle value
                - determine if we want to move to the left or to the right of the middle value
                    - if the middle value is greater than or equal to the value at left pointer
                        - it is part of the left portion and we check the right portion for the min value
                    - otherwise we want to move to the left portion and check for the min value there
        4. return the result
            
        """
        
        res = nums[0]
        l, r = 0, len(nums)-1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: 
                l = m + 1
            else:
                r = m - 1
        return res
            