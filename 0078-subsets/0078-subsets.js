/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums, depth = 0, subset = [], results = []) {
    if (depth === nums.length) {
        results.push(subset)
    } else {
        subsets(nums, depth + 1, subset, results);
        subsets(nums, depth +1, [...subset, nums[depth]], results);
    }
    return results;
};