/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    let result = 0
    nums.forEach(el => {
        if (el.toString().length%2===0) {
            result++
        }
    })
    return result
};