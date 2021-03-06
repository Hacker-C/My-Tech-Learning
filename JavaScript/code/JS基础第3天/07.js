var str =  ''
for (let i = 0; i < 10; i++) {
    for (let j = 0; j <= i; j++) {
        str += '⏰';
    }
    str += '\n';
}
console.log(str);