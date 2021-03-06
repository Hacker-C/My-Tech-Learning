var str = ''
loop1:
for (let i = 0; i < 5; i++) {
    if (i == 2) {
        continue loop1;
    }
    str += i;
}
console.log(str);
