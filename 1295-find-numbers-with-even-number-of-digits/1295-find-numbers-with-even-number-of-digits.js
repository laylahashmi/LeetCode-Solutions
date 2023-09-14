/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    return nums.reduce((acc, num) => num.toString().length%2===0 ? acc+=1 : acc, 0)
};