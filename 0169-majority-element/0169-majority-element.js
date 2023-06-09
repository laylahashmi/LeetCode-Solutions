/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count = {}
    nums.forEach(number => {
        if (!count[number]) {
            count[number] = 1
        } else {
            count[number]++
        }
    })
    let highestValue = 0
    for (let key in count) {
        value = count[key]
        if (value > highestValue) {
            highestValue = value
            highestValueKey = key
        }
    } return highestValueKey
};