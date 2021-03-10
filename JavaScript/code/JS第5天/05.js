function test() {
    for (let i = 0; i < arguments.length; i++) {
        console.log(arguments[i]);
    }
}
test(1, 2, 3, 4);