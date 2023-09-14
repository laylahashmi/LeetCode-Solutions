/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let sorted = [...nums].sort((a, b) => a - b) // use spread operator and sort the new array
                                                // from smallest largest
    return nums.map((num) => sorted.indexOf(num)) // maps a new arr with the first index that the num in the original array occurs at which is the same thing as how many numbers are smaller than it.
};