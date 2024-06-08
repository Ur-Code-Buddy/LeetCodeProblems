/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    
    if (nums.length == 0) {return init}
    let temp_val = init;

    for (let i = 0; i < nums.length; i ++){
        temp_val = fn(temp_val, nums[i]);
    }
    return temp_val;    
};