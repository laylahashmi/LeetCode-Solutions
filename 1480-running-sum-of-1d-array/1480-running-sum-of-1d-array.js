/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
  const values = []
  nums.forEach((value, index) => {
      values[index] = index === 0 ? nums[index] : values[index - 1] + value
  })
  return values
};