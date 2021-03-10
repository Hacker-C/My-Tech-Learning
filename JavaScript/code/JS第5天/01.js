let arr = [2, 0, 6, 1, 77, 0, 52, 0, 25, 7];
let newArr = [];
for (let i=0;i<arr.length;i++) {
    if (arr[i]  >10) 
        newArr[newArr.length] = arr[i];
}
console.log(newArr);