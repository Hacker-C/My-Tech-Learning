//数组去重
let arr = [2, 0, 6, 1, 77, 0, 52, 0, 25, 7];
let newArr = [];
for (let i = 0; i < arr.length; i++) {
    let flag = true;
    for (let j=0;j<newArr.length;j++) {
        if (newArr[j]===arr[i]) {
            flag = false;
            break;
        }
    }
    if (flag) {
        newArr[newArr.length] = arr[i];
    }
}
console.log(newArr);