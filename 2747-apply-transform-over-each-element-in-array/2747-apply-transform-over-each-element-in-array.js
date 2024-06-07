/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    var res_arr = []; 
    for (let i = 0; i < arr.length; i ++){
        const res_val = fn(arr[i],i);
        res_arr.push( res_val );
        
    }
    return res_arr;
};