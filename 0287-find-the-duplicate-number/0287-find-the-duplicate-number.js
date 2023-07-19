/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    //singly linked cycle
    let fast = 0;
    let slow = 0;
    
    while (true) {
        fast = nums[nums[fast]]; //increment fast by 2
        slow = nums[slow]; //increment slow by 1
        
        if (fast===slow) {
            let pointer = 0; //another slow pointer
            
            while (pointer !== slow) {
                pointer = nums[pointer]; //increment pointer by 1
                slow = nums[slow]; //increment slow by 1
            }
            return pointer;
        }
    }
};