/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    return nums.map((num) => num.toString()).reduce((acc, num) => num.length%2===0 ? acc+=1 : acc, 0)
};