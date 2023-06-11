/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const subsetCount = Math.pow(2, nums.length);
    results = [];
    for (let i = 0; i < subsetCount; i++) {
        const binaryString = i.toString(2).padStart(nums.length, "0")
        subset = []
        for (let j = 0; j < binaryString.length; j++) {
            if (binaryString[j] === '1') {
                subset.push(nums[j]) 
            }
        } results.push(subset)
    }
    return results
};