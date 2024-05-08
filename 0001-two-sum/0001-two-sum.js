/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hashmap = {};
    let index = 0;
    for (val of nums){
        let temp = target - val;
        if(temp in hashmap){
            return [index, hashmap[target-val] ];
        }
        else{
            hashmap[val] = index;
        }
        index++;
    }
    
};