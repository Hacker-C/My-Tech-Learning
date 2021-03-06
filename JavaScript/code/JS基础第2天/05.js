// null, false, 0, ''
console.log('' == false);
console.log('' == 0);
console.log(0 == false);
console.log('1' == 1 == true);

console.log('---');

console.log('NaN与其他值比较:');

console.log(NaN == 0); // false
console.log(NaN == ''); // false
console.log(NaN == NaN); // false
console.log(NaN == null); // false
console.log(NaN == false); // false
console.log(NaN == undefined); // false

console.log('null与其他值：');
console.log(null == null); // true
console.log(null == undefined); // true
console.log(null == 0); // false
console.log(null == ''); // false
console.log(null == NaN); // false
console.log(null == false); // false

console.log('undefined与其他值比较:');
console.log(undefined == null);  // true
console.log(undefined == undefined);  // true
console.log(undefined == 0);  // false
console.log(undefined == '');  // false
console.log(undefined == NaN);  // false
console.log(undefined == false);  // false