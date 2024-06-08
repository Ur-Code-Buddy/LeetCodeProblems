/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let temp_val = fn(init, nums[0]);
    if (nums.length == 0) {return init;}
    console.log(`temp_val: ${temp_val}`);

    for (let i = 1; i < nums.length; i ++){
        temp_val = fn(temp_val, nums[i]);
        console.log(temp_val);
    }
    return temp_val;    
};