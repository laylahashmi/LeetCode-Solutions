/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    return nums.map((curr, index, arr) => index > 0 ? arr[index] += arr[index - 1] : arr[index])
};