/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let answer = []
    for (i = 0; i < nums.length; i++) {
        let product = 1
        let j = 0
        while (j < nums.length) {
            if (j===i) {
                j++
            } else {
                product *= nums[j]
                j++
            }
        }
        answer.push(product)
    }
    return answer
};