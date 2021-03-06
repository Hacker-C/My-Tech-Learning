for (let i = 0; i < 5; i++) {
    var str = ''
    for (let j = 0; j < 5; j++) {
        str += '⭐';
    }
    console.log(str);
}

for (let i = 0;i<10;i++) {
    var str = '';
    for (let j = 0; j < 10 - i; j++) {
        str += '⭐';
    }
    console.log(str);
}