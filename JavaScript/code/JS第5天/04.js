//冒泡排序
function bubleSort(nums) {
    for (let i = nums.length-1; i > 0; i--) {
        for (let j = 0; j < i; j++) {
            if (nums[j] > nums[j + 1]) {
                let temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
            }
        }
    }
    return nums;
}
let arr = [2, 0, 6, 1, 77, 0, 52, 0, 25, 7];
let newArr = bubleSort(arr);
console.log(newArr);