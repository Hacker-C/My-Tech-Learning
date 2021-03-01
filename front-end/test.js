var a = new Array(2, 4, 4, 5, 6)
var sum = 0
function test() {
    for (let i = 0; i < a.length; i++)
        sum += a[i];
    return sum;
}
console.log(test());


