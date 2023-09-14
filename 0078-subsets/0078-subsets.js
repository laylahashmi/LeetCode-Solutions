/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    let subsets = [[]];
    
    for (let el of nums) { //2
        let last = subsets.length-1; //1
        for (let i = 0; i <= last; i++) {
            subsets.push([...subsets[i], el]);
            console.log(subsets)
        }
    }
    return subsets;
    
};