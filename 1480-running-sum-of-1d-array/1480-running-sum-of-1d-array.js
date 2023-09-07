/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    for (i = 0; i < nums.length; i++) {
        if (i >= 1) {
            nums[i] = nums[i] + nums[i-1]
        }
    }
    return nums
};