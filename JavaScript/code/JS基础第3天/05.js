var ans1 = 0, ans2 = 0, ans3 = 0, ans4 = 0
for (let i = 1; i < 101; i++) {
    ans1 += i;
    if (i % 2 == 0) {
        ans2 += i;
    } else {
        ans3 += i;
    }
    if (i % 3 == 0) {
        ans4 += i;
    }
}
console.log(ans1 / 100);
console.log(ans2, ans3);
console.log(ans4);