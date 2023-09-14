/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    // let sum = 0;
    // return nums.map((n) => sum+=n)
    return nums.map((curr, index, arr) => index > 0? arr[index] += arr[index-1] : arr[index])
    ;
};