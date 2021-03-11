/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function (nums) {
    let ans = 0, k = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            k++;
        } else {
            if (k > ans) {
                ans = k;
            }
            k = 0;
        }
    }
    if (k > ans) {
        ans = k;
    }
    return ans;
};
console.log(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]));