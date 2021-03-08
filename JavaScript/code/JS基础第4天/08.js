const a = '12';
function printIsNumber(x) {
    if (!isNaN(x)) {
        console.log(x + '是数字型。');
        return;
    }
    console.log(x + '不是数字型');
}
printIsNumber(a)
