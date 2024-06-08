/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let return_arr = [];
    for (let i = 0; i < arr.length; i ++){
        const temp = fn(arr[i],i);
        if (temp){return_arr.push(arr[i]); }
    }
    return return_arr;
    
};