/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
   
   example=[]
   for(let i=0;i<arr.length;i++){
    example.push(fn(arr[i],i))
   
   }
   return example
    
};