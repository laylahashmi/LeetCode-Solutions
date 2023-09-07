/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    let count = 0
    // nums.forEach(el => {
    //     if (el.toString().length%2===0) {
    //         count++
    //     }
    // })
    
    for (i = 0; i < nums.length; i++) {
        let numberOfDigits = nums[i].toString().length;
        if (numberOfDigits%2===0) {
            count++
        };
    };
    return count
};