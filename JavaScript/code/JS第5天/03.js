//反转数组
let arr = [2, 0, 6, 1, 77, 0, 52, 0, 25, 7];
let newArr = [];
for (let i = arr.length - 1; i >= 0; i--) {
    newArr[newArr.length] = arr[i];
}
console.log(newArr);