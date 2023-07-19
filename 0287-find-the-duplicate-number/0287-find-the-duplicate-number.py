class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            
            if fast == slow:
                pointer = 0
                
                while pointer != slow:
                    pointer = nums[pointer]
                    slow = nums[slow]
                return pointer
                    
        