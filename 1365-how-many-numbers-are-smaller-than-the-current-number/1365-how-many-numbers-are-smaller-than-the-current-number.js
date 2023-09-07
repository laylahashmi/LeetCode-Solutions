/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    return nums.reduce((acc, el, index, arr) => 
        [...acc, arr.reduce((sum, k) => k < el ? sum+=1 : sum, 0)], [])
};