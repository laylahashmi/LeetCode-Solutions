/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let output = [];
    for (let i=0; i<nums.length; i++) {
        let count=0
        let j=0
        while (j<nums.length) {
            if (nums[j] < nums[i]) {
                count++
                j++
            } else {
                j++
            }
        } output.push(count)
    } return output
};