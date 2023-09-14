/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let result = 0;
    let count = 0;
    nums.forEach((num) => {
        if (count === 0) {
            result = num;
        } 
        if (result !== num) {
            count --;
        } else {
            count ++;
        }
    })
    return result
};