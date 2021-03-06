function fibonacci(n) {
    var a = [0, 1, 1];
    if (n >= 3) {
        for (var i = 3; i <= n; i++) {
            a[i] = a[i - 1] + a[i - 2];
        }
    }
    return a[n];
}
console.log(fibonacci(5));
